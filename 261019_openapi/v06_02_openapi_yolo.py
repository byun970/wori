import os               # 환경변수(.env) 읽는 도구
import urllib.request   # 인터넷 주소로 자료 요청하는 도구
import json             # 글자로 된 자료를 사전(dict)모양으로 바꾸는 도구
import pandas as pd     # 자료를 엑셀 같은 표로 다루는 도구
from dotenv import load_dotenv  # .env 파일을 읽어 환경변수로 등록하는 도구
from ultralytics import YOLO
import cv2

load_dotenv()  # .env 파일의 키=값을 환경변수로 불러옴

# 1. 인증키
key = os.getenv("ITS_API_KEY")
if not key:
    raise ValueError("ITS_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
# 과금 우려있는 API KEY는 코드 노출 그리고 깃허브에 업로드 하지 않음
# .env 환경변수로 관리

# 2. 도로 유형  (its=일반도로, ex=고속도로) -> 어느 도로 cctv 가져올 건지
road_type = "its"

# 3. 관심 영역(경도, 위도 범위)
minX, maxX = 120.95, 127.02
minY, maxY = 30.55, 37.69
getType = "json"

# 4. API URL 조립
url_cctv = (
    f"https://openapi.its.go.kr:9443/cctvInfo"
    f"?apiKey={key}&type={road_type}&cctvType=1"
    f"&minX={minX}&maxX={maxX}"
    f"&minY={minY}&maxY={maxY}&getType={getType}"
)

# 5. 요청(만든 주소로 "자료 주세요!")
response = urllib.request.urlopen(url_cctv)
print(response)
# 6. bytes -> str
json_str = response.read().decode("utf-8") # bytes -> str
# print(json_str)
json_dict = json.loads(json_str)    # str -> dict (사전 모양)
# print(json_dict)

# 7. 데이터 프레임 변환
cctv_play = pd.json_normalize(
    json_dict["response"]["data"], sep=''
)
# print(cctv_play)
#      roadsectionid      coordx     coordy cctvresolution filecreatetime  cctvtype cctvformat             cctvname                                            cctvurl
# 0                   126.261960  36.751058                                       1        HLS    [국도38] 태안 두야교회교차로  http://cctvsec.ktict.co.kr/4027/GS9cuqRaCq9cmh...
# 1                   126.612830  36.366430                                       1        HLS  [국도 21호선] 보령 봉황터널시점  http://cctvsec.ktict.co.kr/4107/YVJDetuWhH2gGu...
# 2                   126.595440  36.378530                                       1        HLS  [국도 21호선] 보령 봉황터널종점  http://cctvsec.ktict.co.kr/4108/uEw2V7VUiudn1P...
# 3                   126.617068  36.506767                                       1        HLS  [국도 21호선] 홍성 단아래사거리  http://cctvsec.ktict.co.kr/4109/XIgVIAd5Mc+EOX...
# 4                   126.463910  36.775370                                       1        HLS   [국도 29호선] 서산 석림사거리  http://cctvsec.ktict.co.kr/4120/bUjLufPLscQPC/...
# ...            ...         ...        ...            ...            ...       ...        ...                  ...                                                ...
# 1131                126.431750  36.365100                                       1        HLS      [국도77] 보령 원산교차로  http://cctvsec.ktict.co.kr/79943/AIoboCF598a09...
# 1132                126.426860  36.369770                                       1        HLS      [국도77] 보령 원의교차로  http://cctvsec.ktict.co.kr/79944/Cq4IS6LXWRVtz...
# 1133                126.427360  36.379000                                       1        HLS      [국도77] 보령 선촌교차로  http://cctvsec.ktict.co.kr/79945/M3e6nxxBpjsL2...
# 1134                126.422390  36.402780                                       1        HLS      [국도77] 태안 영목교차로  http://cctvsec.ktict.co.kr/79946/zEbVeHDV9LXKv...
# 1135                126.683466  36.978533                                       1        HLS  [국도38] 가곡지하차도(대산방향)  http://cctvsec.ktict.co.kr/79964/Bo6Q2k4U1wfpx...
# 8. CCTV URL 출력
test_url = cctv_play['cctvurl'][999]
print(f"선택한 cctv url : {test_url}")

# 9. 프레임 설정
cap = cv2.VideoCapture(test_url)

# 10. 모델 로드
model = YOLO("yolo11n.pt")

# 11. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인해주세요.")
        break
    results = model(frame)
    annotated_frame = results[0].plot()

    # 11-1. 윈도우 창 설정 및 띄우기
    cv2.namedWindow("OPENAPI", cv2.WINDOW_NORMAL)   # 창 크기 조절
    cv2.imshow("OPENAPI", annotated_frame)

    # 11-2. q키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료합니다.")
        break

# 12. 자원 해제
cap.release()
cv2.destroyAllWindows()
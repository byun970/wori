from ultralytics import solutions

# inference 객체 생성
inf = solutions.Inference(
    model="yolo11n.pt"
)

# 2. 추론 실행
inf.inference()
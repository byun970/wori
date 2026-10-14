# 붕어빵 비유
    # 클래스 : 붕어빵 틀(설계도)
    # 생성자 : 붕어빵을 처음 만들 떄 자동 실행되는 준비 단계(재료 넣기)
    # 속성 : 붕어빵의 맛, 크기, 색상(정보를 담는 변수)
    # 메서드 : 붕어빵이 할 수 있는 일(먹기, 데우기 - 클래스 안의 함수)
    # 객체 : 틀로 만든 진짜 붕어빵(실제로 만들어진 것)

# 클래스 정의
class Bungeoppang:
    # 생성자
    def __init__(self, taste, size, color):
        self.taste = taste
        self.size = size
        self.color = color

    # 메서드 정의
    def info(self):
        print(f"{self.taste}, {self.size}, {self.color}")

# 객체 생성
bungeoppang_1 = Bungeoppang("팥", "중간", "갈색")
bungeoppang_2 = Bungeoppang("초콜릿", "작은", "노랑")

bungeoppang_1.info()
bungeoppang_2.info()
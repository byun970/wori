# 람다함수(일회용 함수)
# 함수 명 = lambda 매개변수 : 반환값

# 기본 함수
# def add(a, b):
#     return a + b
# print(add(3, 5))  # 8

# 람다 함수
# add = lambda a, b: a + b
# print(add(3, 5))  # 8

import pyfiglet
# pyfiglet
# def decorate_text(text):
#     return pyfiglet.figlet_format(text)
decorate_text = lambda text: pyfiglet.figlet_format(text)
print(decorate_text("Hello World"))
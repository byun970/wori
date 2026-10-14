import pyfiglet
from termcolor import colored

# 구현 : pyfiglet + colored를 적용한 sentence 출력
sentence = "Hi"
py_sentence = pyfiglet.figlet_format(sentence)
py_colored_sentence = colored(py_sentence, 'cyan', 'on_red', ['bold'])
print(py_colored_sentence)
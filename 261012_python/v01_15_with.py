# with open("menmo.txt","w", encoding="utf-8") as f:
#     f.write("Hello, World!\n")
#     f.write("This is a test file.\n")
#     f.write("Goodbye!\n")

# with open("menmo.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# print(text)

# 파일 이어 쓰기
with open("memo.txt","a", encoding="utf-8") as f:
    f.write("\n 줄바꿈 가능합니까?")

print("완료")
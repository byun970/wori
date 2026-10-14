# with open("memo1.txt","x", encoding="utf-8") as f:
#     f.write("오늘은 날씨가 맑습니다.\n")
#     f.write("내일은 비가 올 예정입니다.\n")

with open("can1.jpg","rb") as f:
    text = f.read()
print(text)
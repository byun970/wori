colors = ["red", "green", "blue"]

# print(colors[0]) # red
# print(colors[-1]) # blue
# print(colors[0:2]) # ['red', 'green']

# colors[-1] = "black"
# print(colors) # ['red', 'green', 'black']

# colors.append("pink")
# print(colors) # ['red', 'green', 'black', 'pink']

colors.insert(0, "white")
# print(colors) # ['white', 'red', 'green', 'blue']

colors.remove("white")
print(colors) # ['red', 'green', 'blue']


numbers = [8, 5, 3, 2, 7]
numbers.sort()               # 오름차순 정렬
numbers.sort(reverse=True)   # 내림차순 정렬
numbers.reverse()            # 순서 뒤집기
print(2 in numbers)          # True (포함 여부)
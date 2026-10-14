mixed = [1, "hello", 3.14, True]

# for item in mixed:
#     print(item)
# 1
# hello
# 3.14
# True

for index, item in enumerate(mixed):
    print(f"index: {index}, item: {item}")
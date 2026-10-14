names = ["뽀삐","초코","쿠키"]
scores = [45, 78, 90]

# for name, score in zip(names, scores):
#     print(f"{name}: {score}점")
# 뽀삐: 45점
# 초코: 78점
# 쿠키: 90점

# pairs = list(zip(names, scores))
# print(pairs)

pairs = dict(zip(names, scores))
print(pairs)
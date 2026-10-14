# is_raining = False
# if(is_raining):
#     print("우산을 챙기세요")
# else:
#     print("우산 없어도 됩니다")

temperature = 28

if temperature >= 30: # 온도 => 날씨가 좋네요. 산책을 해보세요.
    print("날씨가 더워요. 물을 많이 마시세요.")
elif temperature >= 20:
    print("날씨가 좋네요. 산책을 해보세요.")
elif temperature >= 10:
    print("겉옷 입으세요")
else:
    print("날씨가 추워요. 따뜻하게 입으세요.")
temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요") 
elif 0 <= temp < 10:
    print("추워요. 나가지 마세요")


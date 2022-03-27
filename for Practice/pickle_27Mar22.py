import pickle
profile_file = open("profile.pickle", "wb") # pickle 에서는 binary 설정을 위해 wb로 입력, pickle은 따로 encoding 설정 필요 없음
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

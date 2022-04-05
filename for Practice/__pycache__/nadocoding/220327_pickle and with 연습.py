# import pickle
# profile_file = open("profile.pickle","wb") # pickle 에서는 binary 설정을 위해 wb로 입력, pickle은 따로 encoding 설정 필요 없음
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb") 
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 로 ! 
# print(profile)
# profile_file.close()


# with  열/닫 작업 편하게

# import pickle
# with open ("profile.pickle", "rb") as profile_file: 
#     print(pickle.load(profile_file)) # 닫을 필요 없음
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.") 

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# 퀴즈 ! 

# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간 보고 -
# 부서: 
# 이름:
# 업무 요약: 

# 1주차부터 50 주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
#조건: 파일명은 "1주차.txt", "2주차.txt".. 로 작성한다.

for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file: 
        report_file.write("- {0} 주차 주간 보고 -".format(i))
        report_file.write("\n부서:")
        report_file.write("\n이름:")
        report_file.write("\n업무 요약:")

    
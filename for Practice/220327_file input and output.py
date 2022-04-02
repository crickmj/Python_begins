# # 파일 입출력 
# score_file = open("score.txt", "w", encoding="utf8") # 스코어 파일을 쓰기 (w) 목적으로 열고, (utf8 항상 추가)
# print("수학 : 0", file=score_file) #요렇게 쓴다!
# print("영어 : 50", file=score_file) 
# score_file.close() # 닫아줌 

# 파일 추가

# score_file = open("score.txt", "a", encoding = "utf8") # 기존 파일에 엎어서 쓰고 싶음! append !  
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽어오기
 
# score_file = open("score.txt", "r", encoding="utf8") 
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") 
# print(score_file.readline(), end="") # 줄글로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 몇 줄인지 모를때..! (다른사람 파일)

# score_file = open("score.txt", "r", encoding="utf8") 
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="") 
# score_file.close()

# list 
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line)
score_file.close()
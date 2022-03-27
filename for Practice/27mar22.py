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
 
 score_file = open("score.txt", "r", encoding="utf8") 
 print(score_file.read())
 score_file.close()
#absent = [2,5] # 결석
#no_book = [7] # 책을 깜빡하고 안들고 옴 
#for student in range(1, 11):  # 1- 10까지 출석번호 학생 있을 때
#    if student in absent: 
#        continue # 아래 문장 실행하지 않고, 다음 명령으로 가는 것
#    elif student in no_book:
#        print("오늘 수업 여기까지. {0} 은 교무실로 따라와.".format(student))
#        break
#    print("{0}야 책을 읽어봐".format(student)) 
    
    
    # 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 --> 101, 102, 103, 104 ... 
    
#students = [1,2,3,4,5]
#print(students)
#students = [i+100 for i in students]
#print(students)   


# 학생들 이름을 길이로 바꾸는 연습 
students = ["iron man", "thor", "groot"]
students = [len(i) for i in students]
print(students)
    
    
# 학생 이름 대문자로
students = ["iron man", "thor", "groot"]
students = [i.upper() for i in students]
print(students)

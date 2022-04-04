
# if 참/거짓 

# money = 3000
# card = True

# if money >= 3000 and card == True: # 두 조건 모두 , and or 사용 가능
#     print("택시를 타라")
# else: 
#     print("지하철을 타라")
    

# list, tuple, strings 사용 in or not in 

# print(1 in [1,2,3])

# pocket = ['paper','cellphone','money', 'card']

# if 'card' not in pocket:
#     print("걸어가라") # or pass 사용 
# else: 
#     print("버스타라")

# elif 

# pocket = ['paper', 'money', 'card','cellphone']

# if 'money' in pocket: 
#     print("택시를 타라")
# elif 'card' in pocket: 
#     print("택시를 타라")
# else: 
#     print("걸어라")


# while 

# treeHit = 0

# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 {0}번 찍었습니다".format(treeHit))
#     if treeHit == 10:
#         print("나무 넘어갑니다.") 

# coffee = 10
# money = 300 

# while True:
#     money = int(input("돈을 넣어주세요: "))
#     if money == 300:
#         print("돈을 받았으니 커피를 줍니다.")
#         coffee -= 1
#     elif money > 300:
#         print("거스름돈을 {0} 주고 커피를 드립니다.".format(money - 300))
#         coffee -= 1
#     else: 
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다, 수고!")
#         break
    
# continue

# a = 0
# while a < 10: 
#     a = a + 1
#     if a % 2 == 0: 
#         continue # 위 문장이 맞으면, 아래로 안내려가고 위로 처음부터 다시 시작
#     print(a)
    
# for 

# test_list = ["one","two","three"]

# for i in test_list:
#     print(i)

# a = [(1,2), (3,4), (5,6)]

# for (first, last) in a:
#     print(first - last)
    
# test

marks = [90, 25, 67, 45, 80]

number = 0

# for mark in marks: 
#     number += 1
#     if mark < 60:
#         continue
#     else: 
#         print("{0}번 학생 합격입니다. 축하합니다.".format(number))
        

for number in range(len(marks)): 
    if marks[number] < 60:
        continue
    else: 
        print("{0}번 학생 합격입니다. 축하합니다.".format(number+1))
        
        
# add = 0
# for i in range(0, 11):
#     add = add + i
#     print(add)

# 구구단

for i in range(2, 10):
    for j in range(1 , 10):
        print(i*j, end = " ")
    print(' ')
    
    
a = [1,2,3,4]
result = []

for i in a:
    result.append(i * 3)
    print(result)
    
# or list 내포 

result = [i*j for i in range(2,10)
          for j in range(1,10)]

print(result)


a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
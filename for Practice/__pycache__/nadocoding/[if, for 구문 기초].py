## if elif else

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요") 
elif 0 <= temp < 10:
    print("추워요. 나가지 마세요")

## for

for waiting_no in [0,1,2,3,4]:
    print("대기번호: {0}".format(waiting_no))

## ex1) ranrange ()

for waiting_no in range(6):
    print("대기번호: {0}".format(waiting_no))
    
# ex2)  스타벅스 손님

starbucks = ["아이언맨", "토르", "아이엠 그루트"]

for customer in starbucks:
    print("{0} 님, 커피가 주문되었습니다.".format(customer))
    
## while 문

customer = "토르"
index = 5

while index >= 1: 
    print("{0} 님, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다")
        
        
# ex1 무한루프 

#customer = "아이언맨" 
#index = 1
#while True:
 #   print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
 #   index +=1
    
# ex2

customer = "토르"
person = "unknown"

while person != customer:
    print("{0} 님, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요? ")
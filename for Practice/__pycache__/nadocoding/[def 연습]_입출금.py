def open_account(): ## 함수 정의 
    print("새로운 계좌가 생성되었습니다.")
    
open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다".format(balance+money))
    return balance + money 

def withdraw(balance, money): 
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance-money)) 
        return(balance-money)
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return(balance)

def withdraw_night(balance,money): # 저녁에 출금
    commision=100 # 수수료 100원
    return commision, balance-money-commision

balance = 0 # 잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance,500)

commision, balance = withdraw_night(balance,500)

print("수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format(commision, balance))


# 표준 체중을 구하는 프로그램을 만드시오

# 표준체중: 각 개인의 키에 적당한 체중
# 성별에 따른 공식
# 남자: 키 x 키 x 22
# 여자: 키 x 키 x 21 

# 조건: 표준 체중은 별도의 함수 내에서 계산
# * 함수명: std_weight 
# * 전달값: 키(height), 성별(gender)

#조건 2: 표준 체중은 소수점 둘째자리 까지 표시

# 출력예제 : 키 175 cm 남자의 표준 체중은 67.38 kg 입니다. 

def std_weight(height, gender): 
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175  # cm 
gender = "남자" 
weight = round(std_weight(height/100, gender),2)
print("키 {0} cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
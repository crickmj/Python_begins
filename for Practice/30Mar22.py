# # 예외처리 : 에러 발생 시 처리하는 것 

# try: # try 내부 문장 하다가 , 잘못되면 아래에 except 찾음 
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요."))
#     num2 = int(input("두 번째 숫자를 입력하세요."))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError: # value error 가 있을 때, ValueError 확인 
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)

try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요.")))
    nums.append(int(input("두 번째 숫자를 입력하세요.")))
    # nums.append(int(nums[0] / nums[1]))
    
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
    
except ValueError: 
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except: # 나머지 모둔 에러 이걸로 처리 
    print("알 수 없는 에러가 발생했습니다.")
    #또는
# except Exception as err:
 # print(err) <- 에러 명 나옴 
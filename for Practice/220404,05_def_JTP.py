from math import fabs
from unicodedata import name


def add (a,b): # 매개변수 (parameter) 지정시 순서도 변경 가능, 예를 들어 a=3, b=5 or b=3, a=2
    return a+b

# 이건 걍 내가 만들어 본 거
# x = [1,2,3,4,5]
# y = [1,2,13,5,6]

# number = 0

# for i in range(len(x)):
#     if x[i] == y[i]:
#         print(add(x,y))
#     else: 
#         print("nonono")

# def add (a,b):
#     print("%d + %d 의 값은 %d 입니다." % (a, b, a+b))
# def say():
#     print("hi")
    
def add_many(*arg):
    result = 0
    for i in arg:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

def add_mul(choice, *arg):
    if choice == "add":
        result = 0
        for i in arg:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in arg:
            result = result * i
    return result

result = add_mul('add', 1,4,5)
print(result)

result = add_mul('mul', 1,4,5)
print(result)

# 키워드/딕셔너리는 별 두 개 ! 
def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(first_name = "minjoon")

#함수의 결괏값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b, a*b
# 튜플로 뜨게 하기 싫으면 아래처럼 나눠서 1,2 ㄹ 이렇게 써주면 됨
results1, results2 = add_and_mul(3,4)
print(results1, results2)

#매개변수 초깃값


def say_myself(name, age, man=True):
    print("my name is %s." %name)
    print("i am %d years old." %age)
    if man:
        print("i am a man")
    else:
        print("i am a girl")
        
say_myself("준",32) # 이가지만 쳐도 자동으로 man true 디폴트 설정 
say_myself("준",32, False)

a = 5
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# labda = def 까지 사용하기엔 너무 간단하거나, 사용할 수 없는 곳에서 람다 사용

add = lambda a, b: a+b
results = add(3,4)
print(results)
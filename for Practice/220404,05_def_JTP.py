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


def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(first_name = "minjoon")
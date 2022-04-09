# Q1 
class Calculator:
    def __init__ (self):
        self.value = 0
        
class UpgradeCalculator(Calculator):
    def subs(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.subs(7)

print(cal.value)

# Q2: 객체변수 value가 100 이상 값은 가질 수 없도록 제한하는 MaxLimitCalculatro class 만들어 보자
# 아래 class 사용하여 상속해서 만들어야함

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100
             
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q4 filter/lambda 사용하여 list [1,-2,3,-5,8,-3] 에서 음수 모두 제거

a = [1,-2,3,-5,8,-3]

def positive(x):
    return x > 0

print(list(filter(positive, a)))

print(list(filter(lambda x: x > 0, a)))

# Q 로또 번호 생성  with random

import random
from re import I

lotto = []
while len(lotto) < 6:
    num = random.randint(1,46)
    if num not in lotto:
        lotto.append(num)
        
print(sorted(lotto))


# 구구단 
def Gugu(n):
    result = []
    i = 1
    while i and n < 10:
        result.append(n * i)
        i = i + 1
    return result



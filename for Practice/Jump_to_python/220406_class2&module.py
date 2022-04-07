
# 사칙연산 클래스 생성

from audioop import add

from pyrsistent import thaw


class FourCal:
    def __init__(self, first, second): # __init__ 생성자, 객체 생성될 때 자동으로 호출 
        self.first = first
        self.second = second
        
    def setdata(self, first, second): # a.setdata(first, second) <- 에서 a 객체 self 가 받음. or Fourcal.setdata(a, first, second) 
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def subs(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4,2)

print(a.add())
print(a.mul())
print(a.subs())
print(a.div())


# 상속 

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

c = MoreFourCal(4,2)
print(c.pow())

# inheritance + method overriding

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

d = SafeFourCal(4,0)
    
print(d.div())

import theater_module as tm

tm.price(3)
tm.price_morning(5)
tm.price_soldier(5)
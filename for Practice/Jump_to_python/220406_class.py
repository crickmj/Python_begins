
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2

print(add1(2))
print(add2(4))
print(add1(5))
print(add2(2))

# class !

class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(1))
print(cal1.add(5))
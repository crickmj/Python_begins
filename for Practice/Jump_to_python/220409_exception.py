# try/error 구문

import enum
import sys
from unicodedata import name


try:
    4/0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    
# except 여러개

try: 
    a=[1,2,3]
    print(a[4])
    4/0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.") # 이게 먼저 나왔으나, a=[1,2,3] print(a[4])가 먼저 나왔으므로, 아래 index error가 먼저 뜨고, 얘는 안뜸
except IndexError as e:
    print("list에 없는 값 입니다.")

# except 동시에 띄우기

try:
    a = [1,2,3]
    print(a[4])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print("인덱스가 없거나, 0으로 나눌 수 없습니다.")


# 오류 회피하기

try:
    f = open("나없는파일!.txt", "r")
except FileNotFoundError:
    pass # pass 써서 없어도 그냥 일단 무시하고 넘어감

# 강제 오류 생성 (raise 구문)

class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print("very fast") # 여기 print("very fast") 쳐줘야함, 아니면 오류 발생  
class Bat(Bird):
    def fly(self):
        print("very rapid")
        
eagle = Eagle()
bat = Bat()
eagle.fly()
bat.fly()

class MyError(Exception):
    pass
    
def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print("허용되지 않는 별명입니다.")
 
 # 내장 함수
abs(-2) # 절대값
all([1,2,3])
all([1,2,3,0])
print(chr(97)) # ASCII 코드 
print(dir([1,2,3]))
print(divmod(4,2)) # divmod(a,b) a를 b로 나눈 몫과 나머지 튜플형태로 반환

for i, name in enumerate(['body','head','toe','hands']):
    print(i, name) # 순서가 있는 자료형(리스트, 튜플, 문자열)을 인덱스를 포함하느 Enumerate 객체로 반환 
    
# filter 
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,2,-3,-4,-5,-10,0,10,22]))

# --> 이거를 filter로 

def positive(x):
    return x > 0

print(list(filter(positive, [1,2,-3,-4,-5,-10,0,10,22])))

# library 

import sys
print(sys.argv)

import os

print(os.getcwd())

import shutil
shutil.copy('new.txt','shutil.txt')

# timesleep

# import time
# for i in range(10):
#     print(i)
#     time.sleep(0.3)
    
# import calendar
# print(calendar.calendar(2022))

# import webbrowser
# webbrowser.open("http://www.naver.com")

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()
    
print("End")
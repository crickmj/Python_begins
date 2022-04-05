# set

s1 = set([1,2,3,4,5,6,7])
s2 = set([3,4,5,7,0,9])

# 교집합 
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)

# 값 추가
# - 1개
s1.add(10)
print(s1)
# - 여러 개 # s1.add 쓰면 list 아니라고 안됨
s1.update([8,9,10])
print(s1)

# 특정 값 제거 # 여러개 안되는듯 

s1.remove(1)
print(s1)

# bool type

a = [1,2,3,4,5,6]

while a:
    a.pop()
    if a == [1,2]:
        break
    else:
        continue
        
print(a)

print(bool('pythol'))

print(id(a))

# 동일 id에 저장되어도, 슬라이싱 혹은 copy 써서 지정하면, id 바뀌어서 따로 변경 가능 
from copy import copy

b = a.copy()
print(b)

print(id(a))
print(id(b))

a = [1,2,3]
b = [1,2,3]

print(a is b)
print(id(a))
print(id(b))
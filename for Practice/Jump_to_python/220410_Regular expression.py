# 문자 클래스 []
# [a,b,c] 있을 때, common <- 매칭, dude <- 매칭 안함
# [a - c] -> [a,b,c] '-'은 사이 이어줌. [a-zA-Z] 는 알파벳 전체, [1-5] = [1,2,3,4,5] 와 같음

# /d = [0-9] 0 - 9 동일식 숫자와 매치
# /D = [^0-9] 숫자가 아닌 것과 매칭 

# dot(.) 
# \n을 제외한 모든 문자와 매치 e.g.) a.b = a0b, aab 됨, 하지만 abc의 c는 a,b 밖이므로 안됨
# * 반복
# ca*t = ct 매치 (a가 0번 반복), cat, caaat 모두 매치
# ca+t의 경우, 0번 반복 안됨. 따라서, ct 는 낫매칭, cat, caat 는 매칭 
# {m}은 m 번 반복 매칭 --> ca{3}t = caaat와 매칭, 나머진 안됨
# {m,n}은 m - n 매칭.. ca{1,4}t = cat, caat, caaat, caaaat 매칭, 나머지 안됨 ca?t의 ? 는, {0,1}과 동일 

# re library사용 

import re

# match는 처음부터 검색하기 때문에, 만약 m=p.match("3 ptython")이면 안됨 

p = re.compile('[a-z]+')
m = p.match("python")
if m:
    print("Match found:", m.group())
else:
    print('No match')

# seach 는 전체 검색이라서 찾아줌

m=p.search("3 python")
print(m)

# findall 

result = p.finditer("life is too short")
print(result)
for r in result: print(r)


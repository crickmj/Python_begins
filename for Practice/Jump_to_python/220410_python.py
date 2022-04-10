# 1에서 1000 까지, 3의 배수와 5의 배수인 애들 더하기 
# results = 0
    
# for i in range(1,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         results += i 
#         print(results)

# 총 게시물 수를 '한 페이지 당 보여줄 수 있는 게시물 수'로 나누었을 경우, 전체 페이지가 얼마가 될 지 ?

# def getTotalPage(m, n):
#     if (m % n) == 0:
#         return m // n
#     else: 
#         return (m // n) + 1 

# print(getTotalPage(30, 10))

# import os

# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         ext = os.path.splitext(full_filename)[-1]
#         if ext == '.py':
#             print(full_filename)
    
# search('C:/')

# 정규 표현식

data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split('\n'):
    word_result = []
    for word in line.split( " " ):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


import re

data = """
park 800905-1049118
kim 700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data)) 



print(data.split("\n"))
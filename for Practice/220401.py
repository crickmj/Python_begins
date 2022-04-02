# package 설치 pypi 사용


# from bs4 import BeautifulSoup
# from pandas import DataFrame
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# from matplotlib import seaborn as sb

# 내장 함수, input: 사용자 입력을 받는 함수 

# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때, 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 것 (표시)

# print(dir())
# import random # 외장 함수 
# print(dir())
# import pickle
# print(dir())

# print(dir(random)) #random 모듈 내에서 쓸 수 있는 것들

# 외장함수 써보기, 1st : glob - 경로 내 파일/폴더 목록 조회 (윈도우 dir) 

# import glob 
# print(glob.glob("*.py")) #확장자가 py인 모든 파일


# ㅐ os: 운영체제에서 제공하는 기본 기능

# import os 
# print(os.getcwd()) # 현재 디렉토리 표시 


# folder = "sample_dir"

# if os.path.exists(folder): 
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
    
# else: 
#     os.makedirs(folder) # foler 생성 
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time 시간 관련 함수들 외장 
# import time 
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %h:%m:%s"))

# import datetime
# print("오늘 날짜는", datetime.date.today())

# # timedelta 두 날짜 사이 간격

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난 지 100일은", today + td)


# Quiz 

from mailbox import BabylMessage


import byme
byme.sign

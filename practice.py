
from random import shuffle


user = range(1,21) 

user = list(user)
print(user)
from random import *

shuffle(user)
print(user)

winners = sample(user,4) 

print("당첨자 발표")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print("축하합니다")

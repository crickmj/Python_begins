# import travel.thailand # 모듈/패키지만 가능, 클래스 노노 
#     trip_to = travel.thailand.ThailandPackage()
#     trip_to.detail()

# from travel.thailand import ThailandPackage # 이 구문에서는 사용 가능 
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam # 이 구문에서는 사용 가능 
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *

v = vietnam.VietnamPackage()
t = thailand.ThailandPackage()

print(v.detail(), end = " ")
print(t.detail())

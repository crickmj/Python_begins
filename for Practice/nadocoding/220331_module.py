# 모듈: 필요한 것끼리 부품처럼 잘 맞춰진 파일 느낌, 만들어서 쓸 수 있음! 

# import theater_module
# theater_module.price(3) # 3명이 영화보러 갔을 때 가격
# theater_module.price_morning(4) # 4명 조조할인
# theater_module.price_soldier(5) # 5명 군인


# import theater_module as mv # theater_module 을 mv로 불러올 수 있음

# mv.price(4)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # theater_module 내 모든 걸 사용하겠다.
# #from random import * 과 같음

# price(3)
# price_soldier(4)
# price_morning(5)

# from theater_module import price, price_morning # soldier 필요 없ㅇ르 때

# price(5)
# price_morning(6)

# 또는 하나만 가지고 올 때 그거를 price 로..

from theater_module import price_soldier as price

price(5)
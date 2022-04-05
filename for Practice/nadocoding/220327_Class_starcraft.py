# # starcraft 로 class 연습 
# # 1. 마린 : 공격 유닛, 군인. 총을 쏠 수 있음

# name = "마린"
# hp = 40
# damage = 5

# print("{0}유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크: 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드 

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35 

# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35 

# print("{0}유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))



# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))
    
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# class로 탱크 여러대 ...  마치 붕어빵 틀 있고, 붕어빵 찍어내듯..

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# marine1 = Unit("마린", 40, 5) 
# marine2 = Unit("마린", 40, 5) 
# tank = Unit("탱크", 150, 35)  

## __init__ ..    def __init__(self, name, hp, damage) 여기서 __init__ 쓸 때, self 제외한 나머지 객체들과 동일한 갯수로 지정 필요

# 레이스: 공중 유닛, 비행기. 클로킹 기능 (상대방에게 보이지 않음) 

# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage)) # . 통해서 외부 입력 가능 

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 

# wraith2 = Unit("빼앗은 레이스", 80, 5) 
# wraith2.clocking = True 

# if wraith2.clocking == True:
#     print("{0}는 클로킹 상태입니다.".format(wraith2.name))
    
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attach(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력: {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} 유닛이 {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))
        
# 파이어뱃: 화염방사기, 공격

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attach("5시") 

# 공격 두 번 받는다고 가정 
firebat1.damaged(25)
firebat1.damaged(25)


            
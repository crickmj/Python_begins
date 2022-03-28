# class Unit: 
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")
        
        
# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#        # super().__init__()
#        Unit.__init__(self)
#        Flyable.__init__(self)
       
       
# dropship = FlyableUnit()

# 스타크래프트로 연습

from random import *

class Unit: # 부모 클래스 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) 
        
    def move(self, location):
        print("{0} 유닛: {1} 시 방향으로 {2} 의 속도로 이동합니다.".format(self.name, location, self.speed))
      
    def damaged(self, damage):
        print("{0} 유닛이 {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name)) 
            
class AttackUnit(Unit): # 자식 클래스 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력: {2}]"\
            .format(self.name, location, self.damage))
        
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self): #스팀팩 
        if self.hp > 10:
            self.hp -= 10
            print("{0} 유닛이 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print("{0} 유닛이 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False # 시즈모드 개발여부
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False 
        
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        #현재 시즈 아닐 때 --> 시즈모드
        if self.seize_mode == False:
            print("{0} 유닛이 시즈모드로 전환합니다.".format(self.name)) 
            self.damage *= 2 
            self.seize_mode = True    
        # 시즈모드 --> 해제 
        else:
            print("{0} 유닛이 시즈모드 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False 
            

class Flyable: # 날 수 있는 클래스  
    def __init__(self, flying_speed): 
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} 유닛이 {1} 시 방향으로 날아갑니다. [속도: {2}]"\
            .format(name, location, self.flying_speed))
      
# 공중 공격 유닛 
  
class FlyableAttackUnit(AttackUnit, Flyable): # 공격 및 날 수 있는 거 모두 상속
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 처리 
        Flyable.__init__(self,flying_speed) 
    
    def move(self, location):
        self.fly(self.name, location)
        
# 레이스

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) 
        self.clocked = False
        
    def clocking(self):
        if self.clocked == True:
            print("{0} 유닛의 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False 
        else:
            print("{0} 유닛의 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True 

def game_start():
    print("[알림] 게임을 시작합니다.")
    
def game_over():
    print("player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
    
    

#실제 게임

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
w2 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

# 전군 이동

for unit in attack_units:
    unit.move("1시")
    
# 탱크 시즈 모드 

Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 -> 스팀팩, 탱크 -> 시즈모드, 레이스 -> 클로킹) 

for unit in attack_units:
    if isinstance(unit, Marine): 
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
# 전군 공격 

for unit in attack_units:
    unit.attack("1시") 
    
# 전군 피해 

for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 범위는 5 - 20 

game_over()


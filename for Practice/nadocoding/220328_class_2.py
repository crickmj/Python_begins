# 상속! 
# 일반 유닛 

from turtle import speed


class Unit: # 부모 클래스 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 공격 유닛]")
        print("{0} 유닛: {1} 시 방향으로 {2} 의 속도로 이동합니다.".format(self.name, location, self.speed))
      
class AttackUnit(Unit): # 자식 클래스 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력: {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} 유닛이 {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage 
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

# 다중 상속 ! 
        
# 드랍쉽: 공중 유닛, 수송기, 마린/파이어뱃/탱크 등 수송 , 공격 기능 없음 

class Flyable: # 날 수 있는 클래스  
    def __init__(self, flying_speed): 
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} 유닛이 {1} 시 방향으로 날아갑니다. [속도: {2}]"\
            .format(name, location, self.flying_speed))
      
# 공중 공격 유닛 
  
class FlyableAttachUnit(AttackUnit, Flyable): # 공격 및 날 수 있는 거 모두 상속
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0으로 처리 
        Flyable.__init__(self,flying_speed) 
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 발키리: 공중 공격, 한 번에 14발 

Valkyrie = FlyableAttachUnit("발키리", 200, 6, 5)
Valkyrie.fly(Valkyrie.name, "3")

# 메소드 오버로딩..! --> 지상유닛 스피드 추가

#벌쳐 추가 : 무브 있음
vulture = AttackUnit("벌쳐", 80, 10, 20)
# 배틀크루져 : 무브 없음
Battlecruiser = FlyableAttachUnit("배틀쿠르져", 500, 25, 3)

vulture.move("11")
Battlecruiser.move("9") # 지상/공중 인 것 구분해야해서.. 메소드 오벌됭 해야함


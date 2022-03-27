# 상속! 
# 일반 유닛 

class Unit: # 부모 클래스 
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
      
class AttackUnit(Unit): # 자식 클래스 
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self,flying_speed) 

# 발키리: 공중 공격, 한 번에 14발 

Valkyrie = FlyableAttachUnit("발키리", 200, 6, 5)
Valkyrie.fly(Valkyrie.name, "3")

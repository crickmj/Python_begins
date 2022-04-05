
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
        
# 건물

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 완성된 것 처럼 보임, 오류있든 말든 일단 무시하고 넘김
    
    
# # 서플라이 디팟 : 건물, 1개 건물 당 = 8 만큼의 유닛 생산 가능 

# supply_depot = BuildingUnit("supplydepot", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작하빈다.")

# def game_over():
#     pass

# game_start()
# game_over() # 실행 안되고 그냥 넘어감 

# super 사용 
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self,name,hp,0)
        super().__init__(name, hp, 0) # 슈퍼는 self 정보 없음 
        self.location = location 
        
    
    
# 서플라이 디팟 : 건물, 1개 건물 당 = 8 만큼의 유닛 생산 가능 

supply_depot = BuildingUnit("supplydepot", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over() # 실행 안되고 그냥 넘어감 
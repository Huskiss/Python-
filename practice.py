class Unit:
    def __init__(self,name,hp,speed):
        #__init__은 파이썬에서 쓰이는 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0}유닛이 생성 되었습니다.'.format(self.name))
        print('체력{0}, 속도{1}'.format(self.hp,self.speed))
    
    def move(self, location):
        print('[지상유닛이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

class AttackUnit(Unit): # 클래스 유닛 상속
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self, name, hp, speed) # 클래스 유닛 상속
        self.damage = damage
  
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

class flyable:
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))
    
class FlyableAttackUnit(AttackUnit, flyable): # 클래스 어택유닛, 플라이애이블 상속
    def __init__(self, name, location, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, 0, damage) #지상 속도는 0, # 클래스 어택유닛 상속
        flyable.__init__(self, flying_speed) # 클래스 플라이애이블 상속
        print('{0} : {1} 방향으로 날아갑니다. [속도 {3}, 공격력 {2}]'.format(name, location, damage, flying_speed))
    
벌처 = AttackUnit('벌처', 80, 10, 20)
배틀크루저 = FlyableAttackUnit('배틀크루저', '1시' ,500,25,3)

벌처.move("11시")
배틀크루저.fly('배틀크루저','1시')
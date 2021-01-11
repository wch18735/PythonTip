class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성 되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5) # Unit 클래스의 Instance
marine2 = Unit("마린", 40, 5) # init 함수에 정의된 변수만큼 전달해야 함
tank1 = Unit("탱크", 150, 35)

# 멤버 변수
# self.name, self.hp, self.damage 등
# Class 내에 정의된 변수

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# 마인드 컨트롤
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 추가로 멤버변수를 추가 가능
if wraith2.clocking == True:
    print(f"{wraith2.name} 은(는) 현재 클로킹 상태입니다")


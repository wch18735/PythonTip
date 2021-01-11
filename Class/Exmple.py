# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"     # 유닛 이름
hp = 40          # 유닛 체력 
damage = 5       # 유닛 공격력

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}")

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있으며 일반/시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage= 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}")

def attack(name, location, damage):
    print(f"{name}: {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

attack(name, "1시 방향", damage)
attack(tank_name, "1시 방향", tank_damage)


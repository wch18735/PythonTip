gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_return(gun, soldires):
    gun = gun - soldires
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
# checkpoint(2)
gun = checkpoint_return(gun, 2)
print("남은 총: {0}".format(gun))

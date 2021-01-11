class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()

class FlyableUnit2(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()
dropship2 = FlyableUnit2()
# 다중상속에서는 super().__init__() 을 사용하면 앞의 것만 생성함.
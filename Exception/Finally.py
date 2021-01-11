# Finally: 무조건 실행되는 부분
class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요:"))
    num2 = int(input("두 번째 숫자를 입력하세요:"))
    if num1 >= 10 or num2 >= 10:
        raise CustomError(f"입력값 {num1}, {num2} 에 대한 에러 발생")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except CustomError as err:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
except Exception as err:
    print("에러가 발생하였습니다")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
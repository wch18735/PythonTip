print("나누기 전용 계산기")
try:
    num1 = int(input("첫 번째 숫자:"))
    num2 = int(input("두 번째 숫자:"))
    nums = list()
    nums.append(num1)
    nums.append(num2)
    # nums.append(num1 / num2)
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("Value Error 가 발생하였습니다")
except ZeroDivisionError as err:
    print(err)
except Exception as error:
    # 나머지 모든 에러를 해당 부분에서 처리
    print(error)
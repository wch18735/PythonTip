cabinet = {3: "유재석의 짐",
           100: "김태호의 짐"}

# dictionary 에서 값을 가져오는 방법
print(cabinet[100])

# dictionary 에서 값을 가져오는 방법
print(cabinet.get(3))

# dictonary 에 key 가 없을 때
# 대괄호 [] 를 이용할 때는 오류
# get() 을 사용하면 None 값이 나옴
# 없을 때, key 값을 사용 가능함을 나타내게 할 수 있음
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))

# dictionary에 키가 있느지 확인
print(3 in cabinet)
print(5 in cabinet)

# 정수가 아닌 string 가능
cabinet = {"A-3":"유재석의 짐", "B-100": "김태호의 짐"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 손님
print(cabinet)
cabinet["A-3"] = "김종국의 짐"
cabinet["C-20"] = "조세호의 짐"
print(cabinet)

# 간 손님의 해당하는 key를 삭제
del cabinet["A-3"]
print(cabinet)

# 사용중인 key 들만 출력
print(cabinet.keys())

# 사용중인 value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목용탕 폐점
cabinet.clear()
print(cabinet)
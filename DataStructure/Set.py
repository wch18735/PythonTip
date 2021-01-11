# 집합 (set)
# 중복이 없고, 순서가 없음 (물론 Ordered_set 이 존재하기도 함)

my_set = {1,2,3,3,3}
print(my_set)
print(type(my_set))

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 출력 (java와 python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 개발자가 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)

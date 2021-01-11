# 빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보
example = str()
example = "{0: >10}".format(500)
print(example)

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
example = "{0: >+10}".format(500)
print(example)

# 왼쪽 정렬하고, 빈칸으로 _채움
example = "{0:_<10}".format(500)
print(example)

# 3자리마다 콤마를 찍어주기
example = "{0:,}".format(10000000000)
print(example)

# 3자리마다 콤마를 찍고 +,- 부호 붙이기
example = "{0:+,}".format(1000000000)
print(example)

# 소수점 출력
example = "{0:f}".format(5/3)
print(example)

# 소수점 자리수 출력
example = "{0:.2f}".format(5/3)
print(example)
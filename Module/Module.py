# 일정 부분만 교체하고 추가할 수 있도록 만들어 코드의 재사용, 유지 보수를 쉽게 하는 것
# 파이썬 모듈 확장자: .py

# import theater_module
import theater_module as tm

tm.price(3)
tm.price_soldier(4)
tm.price_morning(5)

from theater_module import price, price_morning, price_soldier
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price_soldier as ps
ps(5)

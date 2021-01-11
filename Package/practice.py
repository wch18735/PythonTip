# # import 예제
# import Package.thailand
# 
# trip_to = Package.thailand.ThailandPackage()
# trip_to.detail()
# 
# # from import 예제
# from Package import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__ 예제
from Package import *
trip_to = vietnam.VietnamPackage()
# trip_to2 = thailand.ThailandPackage() -> __init__.py 의 __all__ 의 범위에 포함되지 않음
trip_to.detail()
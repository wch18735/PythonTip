import inspect
import random
from Package import *

print(inspect.getfile(random))
print(inspect.getfile(vietnam)) # 해당 패키지를 lib 으로 옮겨도 동일한 동작

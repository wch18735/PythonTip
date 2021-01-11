import glob
print(glob.glob("*.py"))

import os
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir("../"))

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())
today = datetime.date.today() # 오늘 날짜
td = datetime.timedelta(days=100) # 100일 저장
print("만난 지 100일 뒤는", today + td)
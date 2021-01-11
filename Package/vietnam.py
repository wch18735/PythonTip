# Vietnam Module
class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 여행 60만원")

if __name__ == "__main__":
    print("Vietnam 모듈 직접 실행")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("Vietnam 외부에서 모듈 호출")
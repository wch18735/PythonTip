import pickle

profile_file = open("profile.pickle", "wb")
profile = {"이름": "Jhon", "나이": 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile_pk = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
print(profile_pk)
profile_file.close()
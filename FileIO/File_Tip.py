# print input
score_file = open("score.txt", "w", encoding="utf8") # encoding="utf8": 한글
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

# write input
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80\n")
score_file.write("코딩: 100")
score_file.close()

# read
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# readline
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 1) 한 줄 읽고 2) 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# readline when don't know a total line number
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
        print(line)
score_file.close()

# readlines
score_file = open("score.txt", "r", encoding="utf8")
for line in score_file.readlines():
    print(line)
score_file.close()
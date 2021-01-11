# 가변인자 활용
def profile(name, age, *language):
    print(f"이름:{name} 나이:{age} 사용언어:", end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 45, "Kotlin", "Swift")
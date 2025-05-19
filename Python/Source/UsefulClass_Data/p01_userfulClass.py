class Cat:
    """
    으앙
    """
    def meow(self):
        print("냥")

# help(Cat)

c = "그니까 이제 알아서 해보삼"

# c가 그니까로 시작하는지
print(c.startswith("그니까"))

# c에서 이제 -> 다음부터
print(c.replace("이제", "다음부터"))

# c에 까가 몇번째에 있나
print(c.find("까"))
print(c.index("까"))

# c에서 3번째 글자
print(c[3])

# c에서 해봐요가 있나
print(c.find("해봐요") != -1)

# c 글자수
print(len(c))

d = "저기"
print(d)
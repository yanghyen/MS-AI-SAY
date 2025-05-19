# 개 이름 : 만득이
# 출력

# 개 나이 : 3살
# 출력

# class : 객체 찍는 도장/붕어빵 틀
class Cat:
    # member
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method
    def singGolgol(self):
        print("그르릉")

    def showInfo(self): # method : 프로그램 상 필요한 기능
        print(self.name)
        print(self.age)

# object : 찍어낸 것/붕어빵
cat = Cat()
cat.name = "나미"
cat.age = 13
cat.singGolgol()
cat.showInfo()
print("----------")

cat2 = Cat()
cat2.name = "=^._.^="
cat2.age = 3
cat2.showInfo()
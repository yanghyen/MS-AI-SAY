# 어벤져스
#   본명
#   나이
#   공격하기
#   출력하기

from os import name


class Avengers:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def attack(self):
        print("공격")

    def showInfo(self):
        print(self.name)
        print(self.age)

# Human
#   name
#   address
#   eat
#   print
class Human:
    def __init__(self, n, a):
        self.name = n
        self.addr = a

    def eat(self):
        print("냐암")

    def showInfo(self):
        print(self.name)
        print(self.addr)

# IronMan is a Avengers
# IronMan is a Human
class IronMan(Avengers, Human):
    pass

i = IronMan("tonny", 40)
i.attack()
i.eat()
i.showInfo()
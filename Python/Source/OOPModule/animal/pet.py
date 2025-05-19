class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def singGolgol(self):
        print("그르릉")

    def showInfo(self): # method : 프로그램 상 필요한 기능
        print(self.name)
        print(self.age)

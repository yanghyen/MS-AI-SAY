class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
    def showInfo(self):
        print(self.name)
        print(self.age)

    def ready(self):
        print("씻고 옷 입고")
        print("나가서 엘베 타고 내려가")

    def goSchool(self):
        self.ready()
        print("버스 타고 학교로")

    def goMart(self):
        self.ready()
        print("걸어서 마트로")

    def goPark(self):
        self.ready()
        print("자전거 빌려서 공원으로")

h = Human("홍길동", 30)
h.showInfo()
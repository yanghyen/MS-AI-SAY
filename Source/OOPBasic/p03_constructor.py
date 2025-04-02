# constructor(생성자)
#   객체가 만들어질 때 작업하고 시픔
#   메소드의 일종

class Phone:
    name = None
    manufacturer = None
    price = None

    def __init__(self):
        print("핸드폰 입고됨")

    def showInfo(self):
        print(self.name)
        print(self.manufacturer)
        print(self.price)

class Computer:
    cpu = None
    ram = None
    hdd = None

    def __init__(self, c, ram, hdd):
        self.cpu = c    # c는 위에 cpu와 무관
        self.ram = ram
        self.hdd = hdd

    def printInfo(self):
        print(self.cpu, self.ram, self.hdd)

hyeins = Phone()
hyeins.name = "iPhone12mini"
hyeins.manufacturer = "Apple"
hyeins.price = 1000000
hyeins.showInfo()

# 객체 한번에 생성
c = Computer("i5-1234", 16, 500)
c.printInfo()
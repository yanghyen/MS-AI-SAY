# is a
# 쇼핑몰
# Pen is a Product
#   -> OOP가 말하는 상속 사용 가능

# 품명이 삼성123, 가격이 500000 하는 상품
# 출력

from typing import Counter


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def showInfo(self):
        print(self.name)
        print(self.price)

class Pen(Product):
    def __init__(self, n, p, c):
        super().__init__(n, p) # Product의 __init__ 호출
        self.color = c
    
    # showInfo 상속받았는데, 이름/가격만 출력 가능
    # 색도 출력되게
    # overriding
    def showInfo(self):
        super().showInfo() # Product의 showInfo 호출 -> 이름, 가격
        print(self.color)

pen = Pen("모나미153", 500, "red")
# pen.showInfo()

phone = Product("삼성123", 500000)
# phone.showInfo()

# 품명이 조던123, 가격이 10만원, 사이즈가 250인 신발
# 정보 출력
class Shoes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def showInfo(self):
        super().showInfo()
        print(self.size)
    
s = Shoes("조던123", 100000, 250)
s.showInfo()

# 품명이 매직스테이션123, 가격이 200만원
# cpu i5-1234, ram 16gb, hdd 500gb 컴퓨터
# 정보 출력
class Computer(Product):
    def __init__(self, name, price, cpu, ram, hdd):
        super().__init__(name, price)
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    
    def showInfo(self):
        super().showInfo()
        print(self.cpu)
        print(self.ram)
        print(self.hdd)

c = Computer("매직스테이션123", 2000000, "i5-1234", 16, 500)
c.showInfo()

# 품명이 그램123, 가격이 250만원
# cpu i7-2345, ram 32gb, hdd 250gb,
# 무게가 3kg 노트북
# 정보 출력

class Laptop(Computer):
    def __init__(self, name, price, cpu, ram, hdd, weight):
        super().__init__(name, price, cpu, ram, hdd)
        self.weight = weight
    
    def showInfo(self):
        super().showInfo()
        print(self.weight)

l = Laptop("그램123", 2500000, "i7-2345", 32, 250, 3)
l.showInfo()
# 이름이 만득이, 나이가 2살인 개
# 정보 출력

# 이름이 홍길동, 집이 인천인 사람
# 정보 출력

class Dog:
    def __init__(self, name, age, clothes):
        self.name = name
        self.age = age
        self.clothes = clothes

    def showInfo(self):
        print("이름이 %s, 나이가 %d인 개" %(self.name, self.age))
        self.clothes.printInfo()

class DogClothes:
    def __init__(self, size, type):
        self.size = size
        self.type = type
    
    def printInfo(self):
        print(self.size, self.type)

class Person:
    def __init__(self, name, residence, pet):
        self.name = name
        self.residence = residence
        self.pet = pet 
        
    def showInfo(self):
        # print(self.name, self.residence, self.pet.name, self.pet.age)
        print(self.name, self.residence)
        self.pet.showInfo()

d = Dog("밤비", 9, DogClothes("XL", "우비"))
d.showInfo()

p = Person("홍길동", "인천", d)
p.showInfo()

# p의 이름
print(p.name)
# p가 키우는 개 이름
print(p.pet.name)
# p가 키우는 개 모든 정보
p.pet.showInfo()
# p가 키우는 개가 입는 옷의 사이즈
print(p.pet.clothes.size)
# p가 키우는 개가 입는 옷의 모든 정보
p.pet.clothes.printInfo()
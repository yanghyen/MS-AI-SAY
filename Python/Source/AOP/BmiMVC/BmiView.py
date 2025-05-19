from GuestModel import Guest


class ConsoleScreen:
    def getGuestInfo():
        name = input("이름 : ")
        height = float(input("키 : "))
        weight = float(input("몸무게 : "))
        return Guest(name, height, weight)
    
    def printFesult(guest):
        print("BMI : %.1f" % guest.bmi)
        print("%s씨는 %s입니다." % (guest.name, guest.result))

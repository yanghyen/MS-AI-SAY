# OOP : real world 묘사
# OOD(Design)
#   guest.bmi 체크하는 걸 객체지향스럽게 설계
#   1) 실제로 비만도 검사센터 가서 검사받는 상황 생각
#   2) 등장인물(프로그램에 필요한 것만 남겨) : 의사, 환자
#   3) 속성(프로그램에 필요한 것만 남겨) : 이름, 나이, ...
#   4) 상황 진행 -> 액션
#   5) ㄱㄱ(최대한 실생활스럽게)


# start()에서 guest를
#   self.guest로 하면 그 의사에게 남는 데이터고
#   guest로 하면 진료 끝나면 사라짐
class Doctor:
    def start(self):
        guest = self.callGuest()
        self.ask(guest)
        self.calculate(guest)
        self.diagnose(guest)
    def callGuest(self):
        return Guest()
    def ask(self, guest):
        guest.tell()
    def calculate(self, guest):
        h = guest.height / 100
        guest.bmi = guest.weight / h**2
        if (guest.bmi >= 39):
            guest.result = "고도 비만"
        elif(30 <= guest.bmi < 39):
            guest.result = "비만"
        elif(24 <= guest.bmi < 30):
            guest.result = "과체중"
        elif(10 <= guest.bmi < 24):
            guest.result = "정상"
        else:
            guest.result = "저체중"
    def diagnose(self, guest):
        print("BMI : %.1f" % guest.bmi)
        print("%s씨는 %s입니다." % (guest.name, guest.result))
# 손님
class Guest:
    # def __init__(self, guest.name, height, weight):
    #     self.guest.name = guest.name
    #     self.height = height
    #     self.weight = weight
    def tell(self):
        self.name = input("이름 : ")
        self.height = int(input("키 : "))
        self.weight = int(input("몸무게 : "))

d = Doctor()
d.start()
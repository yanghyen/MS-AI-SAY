# Garbage Collection
# 메모리 자동정리 시스템

# 이름 모나미153, 색 빨강, 가격 500원인 펜
# 정보 출력
class Pen:
    # 1) 어차피 외부에서 추가 가능한데
    # -> 여기에 쓰는 게 무슨 의미?
    # name = None
    # color = None
    # price = None

    # 2) Python은 overloading이 불가능하니 생성자는 하나만 가능
    # -> 펜 만드려면 이름, 색, 가격 다 알아야 함
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __del__(self):
        print("빠잉")

    def showInfo(self):
        print("이름이 %s, 색이 %s, 가격이 %d" % (self.name, self.color, self.price))

p1 = Pen("모나미153", "빨강", 500)
p1.showInfo()

# 결론
# 1 + 2 => 멤버변수를 따로 안 씀(1) 생성자에서 결정

p2 = Pen("모나미153", "파랑", 1000)
p2.showInfo()

# p1과 속성이 같은 펜
p3 = p1      # p3를 stack에 만들 때 p1의 주소값을 넣은 것. 객체 생성한 게 아님
p3.showInfo()

p1.price = 300
p1.showInfo()
p3.showInfo()

p2 = None       # p2의 stack이 사라져서 이때 GC 발동됨 => 빠잉 출력 
print("hi")
# p3의 price도 300으로 바뀐 이유
# p3 = p1은 p3가 p1과 같은 속성의 개체를 새로 생성한 게 아니라 
# p3가 p1이 가리키는 클래스를 가리키기 때문
# 쌤 : p3를 stack에 만들 때 p1의 주소값을 넣은 것. 새로운 객체 생성한 게 아님
#      p를 p3로도 부르게 한 것

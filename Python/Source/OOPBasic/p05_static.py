# static method
#  계산기
# 1+2 결과 출력
# 멤버변수 없음 => 저장할 게 없음
class Calculator:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    # def __del__(self):
    #     print(self.x + self.y)
    @staticmethod  # 가독성 측면에서 부여 (옵션)
    def printSum(x, y):
        print(x + y)

# 일반 method 호출
# c = Calculator()
# c.printSum(10, 20)

# static method 호출
Calculator.printSum(10, 20)
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name)
        print(self.price)

# 따로 main 영역 따로 안 다루는 자유의 언어라
# Book만 import해도 babo까지 출력됨
# 이를 방지하기 위해
# if __name__ == "__main__":
#     print("babo")


# 이걸 추가하니까 갑자기 에러
# 서로 import 걸면 무한루프 돌게 됨
# Python은 import가 꼭 맨 위에 있지 않아도 돼서
# 이런 식으로 해결
if __name__ == "__main__":
    from p02_oopModule import BoardMarker
    bm = BoardMarker("merong", 13)
    bm.showww()
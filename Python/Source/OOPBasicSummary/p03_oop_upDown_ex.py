# 친구/나 둘이 앉아있는 상황에서 친구가 하자고 함
from random import randint


class Enemy:
    def gameStart(self, u):
        turn = 0
        gameAns = self.thinkAns()
        while True:
            turn += 1
            userAns = self.ask(u)
            if self.judge(gameAns, userAns):
                self.tellResult(turn)
                break
    def thinkAns(self):
        return randint(1, 3)
    def ask(self, u):
        while True:
            userAns = u.tell()
            if 0 < userAns < 4:
                return userAns
            return self.ask(u)
    def judge(self, gameAns, userAns):
        if gameAns == userAns:
            return True
        elif gameAns > userAns:
            print("UP")
        else:
            print("DOWN")
        return False
    def tellResult(self, turn):
        print("%d번만에 정답" % turn)


class User:
    def tell(self):
        return int(input("뭐 : "))
        # u.ans? ans?
        # u.ans => 아까 이 숫자 뽑았다고 계속 들고 가는 것 


e = Enemy()
u = User()
e.gameStart(u)
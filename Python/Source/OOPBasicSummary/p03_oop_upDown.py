# 객체 : 기계, 나
# 컴이 1 ~ 10000 사이 랜덤한 숫자 하나 생각해놓고
# 뭐 : 3423
# UP
# 뭐 : 9000
# DOWN
# 뭐 : 30000    # 범위 밖 숫자는 카운트 ㄴㄴ
# 뭐 : 1243
# UP
# ...
# 뭐 : 5912
# 13번만에 정답

from random import randint


class Computer:
    def startGame(self):
        gameAns = self.pickAns()
        user = self.callUser()
        self.ask(user)
        self.judge(user, gameAns)
    def pickAns(self):
        return randint(1, 3)
    def callUser(self):
        return User()
    def ask(self, user):
        userAns = user.tell()
    def judge(self, user, userAns, gameAns):
        if userAns == gameAns:
            self.tellResult(user)
        elif userAns > gameAns:
            print("DOWN")
            user.turn += 1
        else:
            print("UP")
            user.turn += 1
        self.ask()
    def tellResult(self, user):
        print("%d번만에 정답" % user.turn)



class User:
    def tell(self):
        self.trun = 0
        userAns = int(input("뭐 : "))
        if 0 < userAns < 4:
            return userAns
        return self.tell()

c = Computer()
c.startGame()
# 가위바위보 : 친구, 나
# 친구와 나는 동등
# -> 심판 추가

from random import randint


class Enemy:
    def fire(self):
        return randint(1, 3)

class User:
    def __init__(self):
        self.win = 0
        
    def fire(self):
        return int(input("뭐 : "))

class Referee:
    def callBlueCorner(self):
        return Enemy()
    
    def callRedCorner(self):
        return User()
    
    def start(self):
        blueCorner = self.callBlueCorner()
        redCorner = self.callRedCorner()
        self.tellRule()
        while True:
            bluePaper = self.enemyFire(blueCorner)
            redPaper = self.userFire(redCorner)
            self.tellHand(bluePaper, redPaper)
            end = self.judge(bluePaper, redPaper, redCorner)
            if end:
                self.tellResult(redCorner)
                break

    def enemyFire(self, e):
        return e.fire()

    def userFire(self, u):
        redPaper = u.fire()
        if 0 < redPaper < 4:
            return redPaper
        return self.userFire(u)
    
    def tellHand(self, bluePaper, redPaper):
        print("유저 : %s" % self.ruleBook[redPaper])
        print("컴터 : %s" % self.ruleBook[bluePaper])

    def __init__(self):
        self.ruleBook = [None, "가위", "바위", "보"]
    
    def tellRule(self):
        for i, v in enumerate(self.ruleBook):
            print("%d) %s" %(i, v))
        print("--------")


    def judge(self, bluePaper, redPaper, u):
        t = redPaper - bluePaper
        if t == 0:
            print("무")
        elif t == -1 or t == 2:
            print("패")
            return True
        else:
            print("승")
            u.win += 1
        return False

    def tellResult(self, u):
        print("%d연승" % u.win)

r = Referee()
r.start()
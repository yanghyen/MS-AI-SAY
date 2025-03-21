# 객체지향스럽게 가위바위보
# 친구나 내가 끌고가기엔 어색하니 
# -> 심판 추가
class Referee:
    def startGame(self):
        p1, p2 = self.callPlayers()
    def callPlayers(self):
        return Player1(), Player2()
    def tellRule(self):
        pass
    def player1Fire(self):
        pass
    def player2Fire(self):
        pass
    def judge(self):
        pass
    def tellResult(self):
        pass


class Player1:
    def fire(self):
        pass

class Player2:
    def fire(self):
        pass
    
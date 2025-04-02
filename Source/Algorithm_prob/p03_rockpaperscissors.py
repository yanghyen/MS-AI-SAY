# 1) 가위
# 2) 바위
# 3) 보
# --------------
# 뭐 :
# 나 : 보
# 컴 : 바위
# 승
# --------------
# 뭐 : 3
# 나 : 보
# 컴 : 보
# 무 
# --------------
# ...
# --------------
# 뭐 : 1
# 나 : 가위
# 컴 : 바위
# 패
# 3연승

# 차가 1 : 큰 수가 승
# 차가 2 : 작은 수가 승
# p1 기준
# -1 : 패
# -2 : 승
# 1 : 승
# 2 : 패
# 사용자 패 -> 종료 및 연승 횟수 출력

# 아직 연승 카운트 못했음 ㅠㅅㅠ

from random import randint
#             0       1      2
category = ["가위", "바위", "보"]
def getUserAns():
    userAns = int(input("뭐 : ")) - 1
    print("나 : %s" % category[userAns])
    return userAns

def getGameAns():
    gameAns = randint(1, 3) - 1
    print("컴 : %s" % category[gameAns])
    return gameAns

def judge(player1, player2, cnt, win):
    case = player1 - player2
    if case == 0:
        cnt = 0
        print("무")
    elif case == -1 or case == 2:
        cnt = 0
        print("패")
        return False
    else:
        cnt += 1
        print("승")
    if cnt > 0:
        win += 1
    return True


cnt = 0
win = 0
while True:
    userAns = getUserAns()
    gameAns = getGameAns()
    go = judge(userAns, gameAns, cnt, win)
    if not go:
        print("%d연승" % win)
        break

# 가위바위보 로직 스스로 생각해낸 거 잘했음 ㅎ.ㅎ
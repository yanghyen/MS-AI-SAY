# bool : True/False 2가지 결과만 표현 가능
# -> 3가지 쓰자
# 무 -> 0
# 패 -> 317
# 승 -> 1

# 선생님 답
from random import randint
def comFire():
    return randint(1, 3)

def userFire():
    userHand = int(input("뭐 : "))
    if 0 < userHand < 4:
        return userHand
    return userFire()

def printRule(handTable):
    for i in range(len(handTable)):
        if i != 0:
            print("%d) %s" % (i, handTable[i]))

def printHand(userHand, comHand, handTable):
    # 디코딩(1 -> 가위) 
    print("나 : %s" % handTable[userHand])
    print("컴 : %s" % handTable[comHand])

def judge(userHand, comHand):
    t = userHand - comHand
    if t == 0:
        print("무")
        return 0
    elif t == -1 or t == 2:
        print("패")
        return 317
    else:
        print("승")
        return 1

handTable = [None, "가위", "바위", "보"]
printRule(handTable)
print("------------------")

win = 0
while True:
    userHand = userFire()
    comHand = comFire()
    printHand(userHand, comHand, handTable)

    result = judge(userHand, comHand)
    if result == 317:
        print("%d연승" % win)
        break
    win += result
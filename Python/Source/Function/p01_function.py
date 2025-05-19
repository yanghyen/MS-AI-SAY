def getChocolate():
    print("만원 줄게")
    print("GS 가서")
    print("바클라바 하나 달라 하고")
    print("남은 돈으로 초코 우유 사먹고")
    print("바클라바는 가져왕")
    
getChocolate()

def test():
    pass    # 자리 채우기

# 두 수의 합을 출력하는 함수
def printSum(a, b=10):  # 기본값 지정 가능
    print(a + b)

printSum(20)    # b값 지정 안 하면 기본값으로
printSum(b=90, a=2)    # parameter 지정 가능

# --------------------------------------------
# 세 수의 합을 출력하는 함수
def printSum(a, b, c):
    print(a + b + c)

printSum(1,2,3)
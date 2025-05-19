# 본인 이름 출력하는 함수
def printName(x):
    print("양혜인" * x)

printName(5)
############################
lambda x:print("양혜인" * x)(3)

# 숫자 2개 넣으면 합 구해서 콘솔 출력
lambda x, y:print(x + y)(1, 2)
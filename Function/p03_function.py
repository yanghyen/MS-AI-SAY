# 숫자 넣으면 
# 홀수인지 판별해서 결과 출력하는 함수
def printIsOdd(x):
    if x % 2 == 1:
        print("odd")
    else:
        print("even")

printIsOdd(3)

# 숫자 넣으면
# 홀수인지 판별해주는 함수
def getIsOdd(x):
    isOdd = (x % 2 == 1)
    return isOdd

a = getIsOdd(10)

# 숫자를 하나 넣으면
# x2한 결과를 구해주는 함수
def getDouble(x):
    double = (x * 2)
    return double

b = getDouble(4)

# 숫자 2개 넣으면
# 합을 구해주는 함수
# 호출해서 콘솔에 출력

# return 여러 값X => collection으로
# Python에서 return 여러 값 실행은 되지만
# 자동으로 tuple로 받아짐
def calculate(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = (a, b, c, d)
    return e

(aa, bb, cc, dd) = calculate(20, 30) # 굳이 tuple로 한 이유
c = calculate(2, 3)
print(c)

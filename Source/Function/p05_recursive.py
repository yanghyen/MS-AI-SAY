#-----------------------
# factorial 함수 만드시오
def getFactorial(x):
    if (x == 1):
        return 1
    return getFactorial(x-1) * x
print(getFactorial(4))

# 피보나치 수열 값 구하시오
# 1 1 2 3 5 8 13 21 34 55
# def getFibonacci(x):
#     if (x == 1) or (x == 2):
#         return 1
#     return getFibonacci(x) + getFibonacci(x-1)

def getFibo(x):
    if x < 3:
        return 1
    return getFibo(x-2) + getFibo(x-1)

print(getFibo(3))
# 1부터 n까지 더하기
# 반복문 없이
value = int(input())
sum = 0
if (value >= 0):
    sum += value
    value -= 1
    print(value)
    print(sum)

# -------------------------
# 함수 쓸 것!
def getSum(x):
    if x == 1:
        return 1
    return getSum(x-1) + x

a = getSum(19)
print(a)


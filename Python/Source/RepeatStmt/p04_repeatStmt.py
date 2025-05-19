from random import randint
# 1 + 2 + 3 + ... + ? >= 100
# 을 만족하는 최소 ?를 찾으시오
b = 0
i = 0
while b < 100:
    i += 1
    b += i
print(i)
print("-------------------")

# 1 ~ 10 사이의 랜덤한 정수
c = randint(1, 10)
print(c)
print("-------------------")

# 1 ~ 5 사이의 랜덤한 정수 10번
for i in range(10):
    d = randint(1, 5)
    print(d)
print("-------------------")

# 1 ~ 5 사이의 랜덤한 정수 4 나올 때까지 출력
e = randint(1, 5)
print(e)
while e != 4:
    e = randint(1, 5)
    print(e)
print("--------------------")

# 아무 숫자 입력받아서 출력
# 10이라고 쓰면 그만
f = int(input())
while f != 10:
    f = int(input())
print("--------------------------")


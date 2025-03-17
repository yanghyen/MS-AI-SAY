from random import randint
# 컴이 1 ~ 10000 사이 랜덤한 숫자 하나 생각해놓고
# 5912

# 뭐 : 3423
# UP
# 뭐 : 9000
# DOWN
# 뭐 : 30000    # 범위 밖 숫자는 카운트 ㄴㄴ
# 뭐 : 1243
# UP
# ...
# 뭐 : 5912
# 13번만에 정답

y = randint(1, 10000)
print(y)
cnt = 0
while True:
    answer = int(input("뭐 : "))
    if answer == y:
        cnt += 1
        print("%d번만에 정답" %cnt)
        break
    elif answer > 10000 or answer < 0:
        continue
    elif y < answer < 10000:
        cnt += 1
        print("DOWN")
    elif answer < y:
        cnt += 1
        print("UP")
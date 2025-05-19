# 로또 번호 자동생성기
# set 쓰지 말고, list만 쓰는 쪽으로
# 1 ~ 45 랜덤한 숫자 6개, 중복 X
# 1st : 그냥 뽑
# 2nd : 1st 제외하고 뽑 (불가능)
#       일단 뽑고 -> 1st 와 비교해서 같으면 다시 뽑자
# 3rd : 1st/2nd 숫자만 제외하고 뽑자 (불가능)
#       일단 뽑고 -> 1st/2nd 와 비교해서 같으면 다시 뽑자

from random import randint


def pick(i, lotto):
    ball = randint(1, 6)    # 일단 뽑고
    for j in range(i):
        if ball == lotto[j]:
            return pick(i, lotto)
    return ball
    
lotto = []
for i in range(6):
    lotto.append(pick(i, lotto))

print(lotto)
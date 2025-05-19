for i in range(5):
    for j in range(5):
        for k in range(5):
            if k == 2:
                break   # k for문 종료
            print(i, j, k)
print("------------------------------")

# k가 2되면 i가 깨지게
# 내가 쓴 답
for i in range(5):
    if k == 2:
        break
    for j in range(5):
        for k in range(5):
            print(i, j, k)
print("=====")
# 슨생님 답
iBreak = False
for i in range(5):
    if iBreak:
        break
    for j in range(5):
        if iBreak:
            break
    for k in range(5):
        if k == 2:
            iBreak = True
            break
        print(i, j, k)
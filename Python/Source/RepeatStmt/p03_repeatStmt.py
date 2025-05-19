for i in range(1, 4):
    print(i)

# 9
# 7
# 5
# 3
# 1
for v in range(9, 0, -2):
    print(v)

# 1 + 2 + 3 + 4 + 5 = ?
sum = 0
for i in range(1, 6):
    sum += i
print(sum)
print("----------------")

for i in range(1, 10):
    print("2 x %d = %d" %(i, i * 2))
print("--------------------")

for i in range(1, 10):
    for j in range(1, 10):
        print("%d x %d = %d" %(i, j, i*j))
print("----------------------")

# 구구단 표 출력 
for i in range(1, 10):
    for dan in range(2, 10):
        print("%d x %d = %d" %(dan, i, dan * i), end=" ")
    print()
print("----------------------")

for i in range(5):
    for j in range(5):
        print("ㅋ", end="")
    print()
print("----------------------")

for i in range(5):
    print("ㅋ" * (i+1))
print("----------------------")

for k in range(5, 0, -1):
    print("ㅋ" * k)
print("----------------------")

# ㅋ
#   ㅋ
#     ㅋ 
#       ㅋ
#         ㅋ
for i in range(5):
    print("  " * i + "ㅋ")
print("-----------------------")

# ㅋ
# ㅎㅎㅎ
# ㅋㅋㅋㅋㅋ
# ㅎㅎㅎㅎㅎㅎㅎ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
for i in range(5):
    for j in range(i * 2 + 1):
        if i % 2 == 0:
            print("ㅋ", end="")
        else:
            print("ㅎ", end="")
    print()

for i in range(5):
    if i % 2 == 0:
        s = "ㅋ"
    else:
        s = "ㅎ"
    for j in range(i * 2 + 1):
        print(s, end='')
    print()
print("------------------------")
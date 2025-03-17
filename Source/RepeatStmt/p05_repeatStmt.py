#반복문 제어
from random import randint


for i in range(10):
    if i == 3: 
        break
    print(i)
print("----------------------------")

for i in range(10):
    if i == 3: 
        continue
    print(i)
print("----------------------------")

while True:
    menu = int(input("뭐 : "))
    if menu == 1: 
        print("메뉴 등록")
    elif menu == 2:
        print("메뉴 조회")
    elif menu == 10:
        break
print("----------------------------------")

# 1 ~ 5 사이의 랜덤한 정수 4 나올 때까지 출력
while True:
    a = randint(1, 5)
    print(a)
    if a == 4:
        break

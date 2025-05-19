# shift 이용
value = int(input("값을 입력하세용 : "))
if value >= (1 << 3):
    print("24시간")
    value -= (1 << 3)
if value >= (1 << 2):
    print("흡연실")
    value -= (1 << 2)
if value >= (1 << 1):
    print("주차장")
    value -= (1 << 1)
if value >= (1 << 0):
    print("와이파이")
    value -= (1 << 0)

# -----------------------------------
# shift & 반복문
# value = int(input("값을 입력하세용 : "))

data = ["와이파이", "주차장", "흡연실", "24시간"]
for i in range(len(data) - 1, -1, -1):
    if value >= (1 << i):
        print(data[i]) 
        value -= (1 << i)
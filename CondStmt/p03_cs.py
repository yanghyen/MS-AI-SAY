# 1 : 와이파이
# 2 : 주차장
# 4 : 흡연실
# 8 : 24시간
# 3 : 와이파이 주차장
# 12 : 흡연실 24시간
# shift ?

# 1000 = 1 = 와이파이
# 0100 = 2 = 주차장
# 1100 = 3 = 와이파이, 주차장
# 0111 = 14 = 주차장, 흡연실, 24시간
#       1           2           4       8
'''
cnt = ["와이파이", "주차장", "흡연실", "24시간"]

start = 1
value = 12

if (value & (start << 0)):
    print("와이파이")
elif (value & (start << 1)):
    print("주차장")
elif (value & (start << 2)):
    print("흡연실")
elif (value & (start << 3)):
    print("24시간")
'''
# --------------------------------
value = int(input("값을 입력하세용 : "))
if value >= 8:
    print("24시간")
    value -= 8
if value >= 4:
    print("흡연실")
    value -= 4
if value >= 2:
    print("주차장")
    value -= 2
if value >= 1:
    print("와이파이")

# --------------------------------
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

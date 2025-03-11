# 영수증 
price = int(input("구매한 물건가 : "))
money = int(input("낸 돈 : "))
print("------------------")

change = money - price
print("거스름돈 : %d" %change)
# print("5만원 : %d" %(change // 50000))
# print("1만원 : %d" %(change // 10000))
# print("5천원 : %d" %(change // 5000))
# print("1천원 : %d" %(change // 1000))


# --------------------------------------------------------
# 거스름돈에서 나누기만 하면 추가적인 카운팅이 됨
# 50000원 1장 거슬러주고 남은 돈으로 계산해야 됨 
currency_unit = [50000, 10000, 5000, 1000]
for i in currency_unit:
    cnt = change // i
    change %= i
    print("%d만원 : %d" %(i, cnt))

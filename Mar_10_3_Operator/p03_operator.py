# 영수증 
price = int(input("구매한 물건가 : "))
money = int(input("낸 돈 : "))
print("------------------")

change = money - price
print("거스름돈 : %d" %change)
print("5만원 : %d" %(change // 50000))
print("1만원 : %d" %(change // 10000))
print("5천원 : %d" %(change // 5000))
print("1천원 : %d" %(change // 1000))
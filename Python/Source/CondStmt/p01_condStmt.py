# 중간고사 :
# 기말고사 :
# ------------
# 평균 :

mid = int(input("중간고사 : "))
fin = int(input("기말고사 : "))
avg = (mid + fin) / 2
print("평균점수 : %.1f" %avg)

if (avg > 80):
    print("굿뜨")
elif (avg >70):
    print("노력할 것")
else:
    print("님아")
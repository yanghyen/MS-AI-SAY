height = float(input("키 : "))
age = int(input("나이 : "))
print("키는 %.1fcm, 나이는 %d살" %(height, age))

a = height > 140
c = (age == 5)
d = (age >= 5) and (height >= 130)
e = (age >= 50) or (height >= 140)

# d는 나이가 5살 이상이고, 키도 200 이상이어야
d = (height >= 200) and (age >= 5)

# f는 나이가 10살 이상이고, 20살 이상이면
f = (age <= 20)

# g는 100 <= 키 <= 130 만 탈 수 있음
g = (age <= 130) and (age >= 100)
# Python은 이렇게도 가능
g = (100 <= age <= 130) 

# h는 나이가 5살 이상, 키가 130cm 이하든지 둘 중 하나만
h = (age >= 5) ^ (height <= 130)

# i는 h의 반대
i = not h
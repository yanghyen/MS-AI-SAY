# 이름 :
# 키 :
# 몸무게 :
# -------------
# BMI :
# ~~~씨는 저체중/정상/비만 입니다.

name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("몸무게 : "))
print("--------")

bmi = weight / height**2
print("BMI : %.1f" %bmi)
if (bmi >= 39):
    print("%s씨는 고도비만입니다." %name)
elif(30 <= bmi < 39):
    print("%s씨는 비만입니다." %name)
elif(24 <= bmi < 30):
    print("%s씨는 과체중입니다." %name)
elif(10 <= bmi < 24):
    print("%s씨는 정상입니다." %name)
else:
    print("%s씨는 저체중입니다." %name)
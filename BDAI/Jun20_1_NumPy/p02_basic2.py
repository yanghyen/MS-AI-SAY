a = [10, 20]
b = [30, 40]
c = a + b       # 반복해서 붙이기

print("-------------------")
import numpy as np

aa = np.array([10, 20])
bb = np.array([30, 40])
cc = aa + bb    # 모양이 같으면 같은 자리에 있는 값끼리 계산
dd = aa * 3     # broadcasting: 모양이 다르면 차원수 높은 쪽에서 맞춰서 계산
print(dd)
print("------------------------")

name = np.array(["나미", "몽긒", "구름"])
kor = np.array([100, 20, 50])
eng = np.array([60, 100, 80])
mat = np.array([50, 80, 100])
avg = (kor+eng+mat) / 3
over60 = avg > 70
print(over60)

# masking: True인 index만 
print(name[over60])

# 영어 점수가 50 ~ 70 사이인 학생 이름
# print(name[name[50 < eng < 70]])
print(name[(eng > 50) & (eng < 70)])
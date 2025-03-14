# 10! 구하기
facto = 1
for i in range(1, 11):
    facto *= i
print(facto)

# ----------------------------
b = [1, 5, 64, 24564]

for i in b:
    print(i)
# 보다 밑을 더 선호    
for i in range(len(b)):
    print(b[i])
print("------------------------")
# 값 + 인덱스 버전 (Python만)
for i, v in enumerate(b):
    print(i, v)
print("------------------------")

c = {"기온" : 20, "미세먼지" : "심함"}
for v in c.items():
    print(v, type(v))
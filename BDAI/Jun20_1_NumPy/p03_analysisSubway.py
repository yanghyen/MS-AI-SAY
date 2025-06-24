import numpy as np
# subway.csv

# 역 별로 탄 사람 수 다 더해서
# 역 별로 내린 사람 수 다 더해서 

# 서울역, 종각역

# 내린 사람이 더 많은 역 이름

# ==> 사실 이건 Python이 아니라 DB에서 처리해야 됨
rideSum = {}
alightSum = {}
f = open("C:/Yang/Workspace/BDAI/Jun20_1_NumPy/data/subway.csv", "r", encoding='utf-8')
data = f.readlines()
for i, line in enumerate(data):
    line = line.replace("\n", "").split(",")
    if line[1] == "02":
        break
    if line[4] in rideSum:
        rideSum[line[4]] += int(line[5])
        alightSum[line[4]] += int(line[6])
    else:
        rideSum[line[4]] = int(line[5])
        alightSum[line[4]] = int(line[6])

f.close()
name = []
ride = []
alight = []
for k, v in rideSum.items():
    name.append(k)
    ride.append(v)
    alight.append(alightSum[k])

name = np.array(name)
ride = np.array(ride)
alight = np.array(alight)
print(name[ride < alight])
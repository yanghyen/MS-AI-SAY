# sort 해보기

from datetime import datetime


# f = open("C:/Yang/subway.csv", "r", encoding="utf-8")
# subwaySum = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0, "Sun":0}
# subwayCnt = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0, "Sun":0}
# subwayAvg = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0, "Sun":0}
# for line in f.readlines():
#     line = line.replace("\n", "").split(",")
#     if line[1] == "02":
#         break
#     when = line[0] + "-" + line[1] + "-" + line[2]
#     when = datetime.strptime(when, "%Y-%m-%d")
#     yoil = datetime.strftime(when, "%a")
#     subwaySum[yoil] += (int(line[5]) + int(line[6]))
#     subwayCnt[yoil] += 1
#     subwayAvg[yoil] = subwaySum[yoil] // subwayCnt[yoil]
# f.close()

# f = open("C:/Yang/subwayResult.csv", "a", encoding="utf-8")
# for yoil, sum in subwaySum.items():
#     print(yoil, sum / subwayCnt[yoil])
#     f.write("%s, %.2f\n" %(yoil, sum / subwayCnt[yoil]))
# f.close()

f = open("C:/Yang/subwayResult.csv", "r", encoding="utf-8")
for r in f.readlines():
    r = r.replace("\n", "").split(",")
    print(r, type(r))

# 각 요일별 이용객수(탄+내린) 평균
# 월 0000000
# 화 0000000
# 2015.01.01 목
from datetime import datetime


f = open("C:/Yang/subway3.csv", "r", encoding="utf-8")
data = f.readlines()
sum = {
    "mon" : 0,
    "tue" : 0,
    "wed" : 0,
    "thu" : 0,
    "fri" : 0,
    "sat" : 0,
    "sun" : 0
}
cnt = {
    "mon" : 0,
    "tue" : 0,
    "wed" : 0,
    "thu" : 0,
    "fri" : 0,
    "sat" : 0,
    "sun" : 0
}
for line in data:
    line = line.split(",")
    getOn = int(line[5])
    getOff = int(line[6].replace("\n", ""))
    date = line[0] + line[1] + line[2]
    date = datetime.strptime(date, "%Y%m%d")
    dateWeek = date.isoweekday()
    stationName = line[4]

    if (dateWeek == 1):
        sum["mon"] += getOn + getOff
        cnt["mon"] += 1
    elif (dateWeek == 2):
        sum["tue"] += getOn + getOff
        cnt["tue"] += 1
    elif (dateWeek == 3):
        sum["wed"] += getOn + getOff
        cnt["wed"] += 1
    elif (dateWeek == 4):
        sum["thu"] += getOn + getOff
        cnt["thu"] += 1
    elif (dateWeek == 5):
        sum["fri"] += getOn + getOff
        cnt["fri"] += 1
    elif (dateWeek == 6):
        sum["sat"] += getOn + getOff
        cnt["sat"] += 1
    else:
        sum["sun"] += getOn + getOff
        cnt["sun"] += 1

avg = {
    "mon" : sum["mon"] // cnt["mon"],
    "tue" : sum["tue"] // cnt["tue"],
    "wed" : sum["wed"] // cnt["wed"],
    "thu" : sum["thu"] // cnt["thu"],
    "fri" : sum["fri"] // cnt["fri"],
    "sat" : sum["sat"] // cnt["sat"],
    "sun" : sum["sun"] // cnt["sun"],
}
print(avg)
f.close()
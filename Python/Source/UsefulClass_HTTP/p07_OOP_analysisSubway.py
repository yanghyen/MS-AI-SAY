# OOP 수정
# 각 요일별 이용객수(탄+내린) 평균
# 월 0000000
# 화 0000000
# 2015.01.01 목

from datetime import datetime

def getAvg(filePath):


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

    f.close()
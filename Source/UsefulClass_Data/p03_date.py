from datetime import datetime
# 패키지명 : X
# 모듈명 : datetime.py
# 클래스명 : datetime
# today의 정체 : datetime 내 메소드
now = datetime.today()
# # print(now)
# print(now.year)

d = datetime(2000, 1, 1)
print(d)

# date 객체로 ...
d2 = "1999, 12, 31"
d2 = d2.split(',')
d2 = datetime(int(d2[0]), int(d2[1]), int(d2[2]))
print(d2)

# 날짜 패턴 쓰는 스타일
d3 = "2025/03/23"
d3 = datetime.strptime(d3, "%Y/%m/%d")
print(d3)

d4 = datetime.today()
print(d4)
print(f"{d4.year}.{d4.month}.{d4.day}")

d5 = datetime.today()
d5 = datetime.strftime(d5, "%Y.%m.%d")
print(d5)

# 한국 나이 구하기
# 생일(yyyy-MM-dd) :
# ------------------
# 한국 나이 :

# birth = input("생일(yyyy-MM-dd) : ")
# birth = datetime.strptime(birth, "%Y-%m-%d")
# year = datetime.today().year
# print("------------------")
# print("한국 나이 : %d" % (year - birth.year + 1))
# 날짜로서 의미가 없으면 날짜로 안 해도 됨

# 무슨 요일에 태어났나
birthday = "2001/03/17"
birthday = datetime.strptime(birthday, "%Y/%m/%d")
weekOfDayIndex = birthday.isoweekday()
weekOfDay = ["월", "화", "수", "목", "금", "토", "일"]
print(weekOfDay[weekOfDayIndex - 1])
# %A 찾아보기
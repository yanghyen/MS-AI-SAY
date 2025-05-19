txt = input("뭐 : ")

# 파일 열기
f = open("C:\\Yang\\0325.txt", "a", encoding="utf-8")
# f = open("C:/Yang/0325.txt") 도 가능

f.write(txt + "\r\n")
f.close()   # 다 썼으면 닫으세용 
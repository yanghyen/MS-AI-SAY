f = open("C:/Yang/0325.txt", "r", encoding="utf-8")

data = f.readlines()
for line in data:
    line = line.replace("\n", "")
    print(line)

f.close()
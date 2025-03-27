f = open("C:/Yang/subway.csv", "r", encoding="utf-8")
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    if line[1] == "04":
        break
    print(line)
f.close()
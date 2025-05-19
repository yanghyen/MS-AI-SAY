# 0326.py 읽어서
# 횟수 기준 내림차순
class Word:
    def __init__(self, line):
        line = line.replace("\n", "").split("\t")
        self.word = line[0]
        self.count = int(line[1])

    def show(self):
        print(self.word, ":", self.count)


f = open("C:/Yang/0326.txt", "r", encoding="utf-8")
words = []
for line in f.readlines():
    w = Word(line)
    words.append(w)
f.close()

words.sort(key=lambda w:w.count, reverse=True)

for i, w in enumerate(words):
    if i == 10:
        break
    w.show()

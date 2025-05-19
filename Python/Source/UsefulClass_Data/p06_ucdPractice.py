# 실전 들어가면 테스트 할 때마다 전체 다 하기엔 어려움
# 중간 테스트
# 실전에선 Python으로 불가능 -> Hadoop으로 해야 됨
# Hadoop : 서버급컴 여러대로 병렬 처리

f = open("C:/Yang/KakaoTalkChats.txt", "r", encoding="utf-8")
words = {}
for i, line in enumerate(f.readlines()):
    # if i == 499:
    #     break
    msg = None
    if i > 4:
        line = line.replace("\n", "")
        if (not line.startswith("20")) and (line != ""):
            msg = line
        else:
            try:
                line = line.split(" : ")
                msg = line[1]
                for ii, word in enumerate(line):
                    if ii > 1:
                        msg += " " + line[ii]
            except:
                pass
        if msg != None:
            msg = msg.strip().split(" ")
            if word in words:   # 그런 키값이 dict에 있나
                words[word] += 1 
            else:  
                words[word] = 1

f.close()

# dict에 있는 거 읽어서
# 단어 객체
#   단어
#   횟수

# words라는 dict에 있는 거를
# 0326.csv에 기록
print(words)

f = open("C:/Yang/0326.txt", "a", encoding="utf-8")
for word, count in words.items():
    f.write("%s\t%d\n" % (word, count))
f.close()
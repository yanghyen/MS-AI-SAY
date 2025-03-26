data = input().split(',')
print("---------------")

sum = 0
cnt = 0
for v in data:
    try:
        v = int(v)
        sum += v
        cnt += 1
    except:
        pass

print("합계 : %d" % sum)
print("평균 : %.1f" %(sum / cnt))


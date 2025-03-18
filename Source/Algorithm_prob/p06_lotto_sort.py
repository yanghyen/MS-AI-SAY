# list 넣어주면 정렬해주는 함수
l = [34, 12, 1, 3, 23, 45]

# 정렬하는 함수 정의
def sortList(l):
    for i in range(len(l) - 1):
        if (l[i] > l[i + 1]):
            b = l[i]
            l[i] = l[i + 1]
            l[i + 1] = b
            print(l)
            



a = sortList(l)
print(a)
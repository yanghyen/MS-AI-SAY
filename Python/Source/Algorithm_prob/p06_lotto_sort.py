# list 넣어주면 정렬해주는 함수
l = [34, 12, 1, 3, 23, 21]

# 정렬하는 함수 정의 : bubble sort(제일 저질)
def bubbleSort(l):
    for i in range(0, len(l) - 1):
        if (l[i] > l[i + 1]):
            # b = l[i]
            # l[i] = l[i + 1]
            # l[i + 1] = b
            l[i], l[i + 1] = l[i + 1], l[i] # Python만 가능
        elif (l[0] > l[1]):
            bubbleSort(l)
        # 왜 0번째에 12가 계속 머물렀지?
# bubbleSort(l)
# print(l)

# selection sort
# 리스트 내 가장 작은 수를 찾고 맨 앞으로 보내
def selectionSort(l):
    for turn in range(len(l) - 1):
        for i in range(len(l) - 1 - turn):
            min = l[i]
            if min > l[i + 1]:
                min = l[i + 1]
            l[i] = min
        

selectionSort(l)
print(l)
# list 넣어주면 정렬해주는 함수
l = [34, 12, 1, 3, 23, 45]

# 정렬하는 함수 정의

# bubble sort
# 앞에서부터 두개씩 비교하며 자리 바꿈
def bubbleSort(l):
    for turn in range(len(l) - 1):
        for i in range(len(l) - 1 - turn):
            if l[i] > l[i + 1]:
                l[i] , l[i + 1] = l[i + 1], l[i]

# bubbleSort(l)
# print(l)

# selection sort
# 리스트 내 가장 작은 수를 찾고 맨 앞으로 보내
def selectionSort(l):
    for turn in range(len(l) - 1):
        min = l[turn]   # turn번째가 제일 작다 치고
        minIndex = turn # 최소값이 turn번째에 있다
        for i in range(turn + 1, len(l)):
            if min > l[i]:
                min = l[i]
                minIndex = i
        l[turn], l[minIndex] = l[minIndex], l[turn]
selectionSort(l)
print(l)
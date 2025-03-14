# # Call By Value, Call By Reference
# def test(a, b):
#     print(a, b[0])
#     a = 100
#     b[0] = 100
#     print(a, b[0])
# #################
# a = 10
# b = [10, 20]
# print(a, b[0])
# test(a, b)   
# print(a, b[0]) # 10 10 10 10 100 100 10 100
# # 왜 마지막 100?
# # line 5에서 heap 영역 내 b list의 0번째 값이 100으로 수정돼서 그게 함수 밖에서도 적용
# # 함수 내에서 변수 건드리면 원본에 타격 감 

d = 10
e = 10
def test2(a, b, c):
    global e        # 위에 정의된 e 쓰겠다
    print(a, b[0], c[0])
    a = 100
    b[0] = 100
    c = [100, 200]
    d = 100         # 위에 정의된 d와 무관
    e = 100
    print(a, b[0], c[0], d, e)
#################
a = 10
b = [10, 20]
c = [10, 20]
print(a, b[0], c[0])
test2(a, b, c)   
print(a, b[0], c[0], d, e) # e는 100 출력
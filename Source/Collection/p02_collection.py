# dict : 키-값, 순서X
# 국영수
student = {"양혜인" : [100, 100, 100],
           "양나미" : [0, 100, 500],
           "송이니" : [100000, 2, 9]}
print(student["송이니"][2]) # 송이니 수학

# ------------------------------------
# 유지보수의 시대, Python은 객체지향언어
# 2차원 넘기지 X
print(student.keys()) # 키값 추출
print(list(student.keys()))
print("김밍송" in student) # 학생 중에 김밍송이 있나

# ------------------------------------
a = range(1, 15, 2)
print(list(range(1, 20)))

# ------------------------------------
# tuple
q = 100
w = 200
# q랑 w 값 바꾸기

# Me
# z = [q, w]
# q = z[1]
# w = z[0]

# 다른 PL
# e = q
# q = w
# w = e 
# Python tuple활용
(q, w) = (w, q)

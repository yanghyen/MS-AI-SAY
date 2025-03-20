class Student:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        #여기 있는 속성들은 생성자안에만 있는 속성

    def printStudentInfo(self):
        print(f"이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.mat}")
        #여기서 속성을 불러오고 싶으면 "객체.속성"을 통해서만 불러올수있음. 

    def sum(self):
        print(self.eng+self.kor+self.mat)
# 학생 객체 생성
s = Student("홍길동", 90, 23, 12)
# 객체 리스트 생성
# 리스트를 사용하면서 더 가독성이 좋아지고 
# 정렬이 가능해짐. 
score = [
    s,
    Student("김길동", 10, 9, 8),
    Student("최길동", 1, 900, 800),
    Student("박길동", 10000, 9000, 8000)
]

# 2번 학생(인덱스 1)의 국어 점수 출력
print("2번 학생 국어 점수:", score[1].kor)

# 3번 학생(인덱스 2)의 전체 정보 출력
print("3번 학생 정보:")
score[2].printStudentInfo()



# 학생을 넣으면 
# 총점이 구해지는 함수 
# def getScoreSum(s):
#     return s.kor + s.eng + s.mat
# print(getScoreSum(score[1]))

# 이걸 lambda 함수로
v = (lambda s:s.kor + s.eng + s.mat)(score[1])
print(v)

#이제는 정렬을 해보자. 
# 성적순으로 정렬(list에 있는 학생 하나씩 빼서 자동으로 해줌) 
# 근데 속성들중 어떤 걸 기준으로 정렬을 할것인가.를 괄호 안에 넣어주기 
score.sort(key=lambda s:s.kor + s.eng + s.mat, reverse=True)


# 이름 가나다 역순
score.sort(key=lambda s:s.name, reverse=True)
for s in score:
    s.printStudentInfo()
    print('-----------------------------')

### collection
- List 계열 : list
- Set 계열 : set
- Map 계열 : dict
### list
- len(eng) : 내용물 개수 
- eng[0] : 0번 데이터 
- eng[1:4] : 1~(4-1)번 데이터
- eng[3:9:2] : 3~(9-1)번까지 2칸씩
- eng[:9:2] : 0~(9-1)번까지 2칸씩
- eng.index(30) : 30은 몇번 데이터?
- Java의 배열(수정불가)과 다르게 수정 가능
    - 맨 뒤에 추가 : eng.append(99)
    - 특정 위치에 추가 : eng.insert(2, 88)
    - 수정 : eng[1] = 0
    - 삭제 : del eng[0]
- str을 list처럼 사용하기도
### set
- 중복 제거 (뭔가 좀...)
- 무작위 순서
- list -> set -> list 중복 없애는 용으로 쓰이긴 함
    ```py
    a = [1, 2, 2, 1, 3]
    a = list(set(a))
    ```
### dict
- key : value
- 순서 개념X
```py
student = {"반장":"나미", "부반장":"카피바라"}
print(student["반장"])
print(list(student.keys())) # 키만 추출해서 리스트
print("김밍송" in student) # 학생 중에 김밍송이 있나
>>>
나미
```
- 유용한 코드
    - print(list(student.keys())) # 키만 추출해서 리스트
    - print("김밍송" in student) # 학생 중에 김밍송이 있나
### JAVA vs Python
- JAVA : 규칙의 언어
- Python : 자유의 언어
### range
- 범위 표현, 규칙적인 list 생성
```py
a = range(1, 15, 2) # 1~15, 2칸씩
b = list(range(1, 20))
```
### tuple
- 특징은 list와 동일, 수정 불가
- 데이터 저장용 X
- 변수 여러개 한번에 값 넣을 때
    - (q, w) = (w, q)
- tuple의 소괄호는 생략 가능
    - q, w = w, q
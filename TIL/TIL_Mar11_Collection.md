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
### dict
- key : value
- 순서 개념X
```py
student = {"반장":"나미", "부반장":"카피바라"}
print(student["반장"])
>>>
나미
```
### JAVA vs Python
- JAVA : 규칙의 언어
- Python : 자유의 언어
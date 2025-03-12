### 함수 vs 메소드
- 변수(variable) : 데이터 담는 그릇 => 명사형
- 함수(function) : 액션들 모아놓은 그릇 => 동사형
- 메소드(method) :

### 메인 함수 영역
- 다른 PL : main 함수 영역이 따로 있음
    - main 영역 내에 함수 정의X
    - 띄어쓰기, 엔터 무의미
    <= 영역을 {}로 표시
    - parameter(개수, 자료형) 다르면 함수명 같아도 됨
- Python : interpreter방식 언어라 따로 없음
    - interpreter방식 : 소스 한 줄씩 직접 해석 후 실행
    - 띄어쓰기, 엔터 유의미
    <= 영역을 :과 들여쓰기로 표시
    1. 정의 
    - 함수명 규칙 == 변수명 규칙 
    - parameter : 함수 수행시 필요한 재료
    2. 함수 호출
    ```py
    def test():
        pass    # 자리 채우기
    ```
    - overloading 불가
### 참고
- 작명 팁
    - 동사 앞으로 정렬 -> 기능별 정렬
    - 동사 뒤로 정렬 -> 주제별 정렬
        printSum VS sumPrint
- overriding VS overloading
    - overriding : 부모 클래스의 메소드를 **자식 클래스**에서 재정의하는 것
    - overloading : 
- Call By Value, Call By Reference
    - Call By Value : 함수 호출 시 값 넣어서 호출
    - Call By Reference : 함수 호출 시 주소값 넣어서 호출 (Python)
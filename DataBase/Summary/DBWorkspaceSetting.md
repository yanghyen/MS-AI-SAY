## DB 환경 세팅
- 작업 환경 : DBeaver
- 관리자 계정은 cmd에서만 할 수 있다는 점도 기억해야 한다.

## SQL
- Structured Query Language
- DB 제어할 때 쓰는 언어, PL 아님
- 중에 CRUD하는 부분만 목표
- 대소문자 구분x
- table
    - field, column(열)
    - record, data, row(행)

## CRUD
### Create
- 필드명 규칙
    - 테이블명에서 따옴
    - snack 테이블 -> s_name, s_price
- 용량
    - 숫자, 영어, ... : 1글자가 1byte
    - 한글, 한자, ... : 1글자가 3bytes
    - 기본 : byte
    - 7 char : 7글자(자료형char 아님) -> 21bytes
    - char(7 char) : 이런 식으로 쓰기
- OracleDB 자료형
    - 글자 : char(용량), varchar2(용량)  
    char(용량) : 띄어쓰기를 넣어서라도 용량대로 저장   
        데이터 자릿수가 일정할 때   
        char(5 char)에  
            -> ㅋㅋ저장 -> ㅋㅋ   로 저장됨  
            -> 용량 낭비, 데이터 변형  
    varchar2(용량) : 용량 조절 가능  
        varchar2(5 char)에  
            -> ㅋㅋ저장 -> ㅋㅋ(6bytes만)저장  
            -> 용량 낭비X, 데이터 변형X  
            -> char 보다 느림  
        Oracle에만 있는 varchar 알고리즘 개선판
    - 숫자 : number(용량)  
        number(3) -> ~999 (3자리까지 표현되는 정수)
        number(5, 2) -> 999.99 (전체자리수, 소수점이하) 
    - 날짜/시간 : date    
        현재 시간 날짜(insert하는 시점의 서버시간) : sysdate  
        특정 시간 날짜 :   
            to_date(값, 패턴) : str -> datetime  
            패턴 : Y M D AM PM HH  MI SS  
    - 동영상, 음악, ... 기타 파일 : DB서버에는 파일명만 저장하고 파일은 웹 서버에 올림
- 테이블 생성
```sql
CREATE TABLE 테이블명(
    열 제목 자료형  [옵션],
    필드명  자료형  [옵션],
    ...
);
```
- 옵션   
    not null : 핖수  
    primary key : not null + 중복 불가  
        -> 데이터를 대표하는 값  
        -> 테이블 하나 만들면 PK는 지정  
- sequence 만들기
```sql
-- sequence 생성
create sequence 시퀀스명;
-- sequence 삭제
drop sequence 시퀀스 명;
-- sequence 사용
(insert 할 때) 시퀀스명.nextval
```

```sql
CREATE TABLE apr01_snack(
    s_name varchar2(10 char),
	s_price number(5)
);
```
- 테이블 수정 : 기능 상 가능하지만, 실전에선 불가능
- 테이블 삭제
```sql
DROP TABLE 테이블명 CASCADE CONSTRAINT purge;
```
- 데이터 추가
```sql
------------- 데이터 추가 --------------
INSERT INTO apr01_snack(S_NAME , S_PRICE)
VALUES ('mychu',500);
-- 데이터 추가 시 순서 상관 없음
INSERT INTO apr01_snack(S_PRICE, S_NAME)
VALUES (500, 'mychu');
```

### Read
- 데이터 조회
    통계 함수 : max, min, sum, avg, count
```sql
SELECT 필드명, 필드명 AS 별칭, 연산자, 통계함수, ...
FROM 필드명
-- 학생 모든 정보
SELECT * FROM student;

-- 학생 이름, 영어 점수(필드명 english)
SELECT s_name, s_eng AS english FROM student;

-- 학생 이름, 국어, 영어, 수학, 평균
SELECT s_name, s_kor, s_eng, s_mat, (s_kor + s_eng + s_mat) / 3 AS s_avg
FROM apr01_student;

-- 학생들 국어 반평균
SELECT avg(s_kor)
FROM apr01_student;
```
## SQL
- Structured Query Language
- DB 제어할 때 쓰는 언어, PL 아님
- 중에 CRUD하는 부분만 목표
- 대소문자 구분x
- table
    - field, column(열)
    - record, data, row(행)

## CRUD
- 실행결과
    - CUD : 데이터 몇개 영향 받았는지 결과가 뜸
    - R : 데이터
### Create : INSERT 
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

### Read : SELECT 
- 데이터 조회
    통계 함수 : max, min, sum, avg, count  
    select만 가능. where에선 불가능
```sql
SELECT 필드명, 필드명 AS 별칭, 연산자, 통계함수, ...
FROM 필드명
WHERE 조건식
ORDER BY 필드명, 필드명; -- 정렬

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
- 문자열 포함 검색 : 필드명 like 패턴  
    패턴 : %활용  
    'ㅋ%' -> ㅋ로 시작  
    '%ㅋ%' -> ㅋ 포함  
```sql
-- 김씨나 최씨
-- 이름, 국/영/수 평균
SELECT s_name, (s_kor + s_eng + s_mat) / 3 AS s_avg
FROM APR01_STUDENT as2 
WHERE s_name LIKE '김%' OR s_name LIKE '최%';
```
- 날짜 함수  
    to_date() : 글자 -> 날짜  
    to_char() : 날짜 -> 글자  
    concat('ㅋ','ㅎ','ㅇ') : 글자 붙일 때 씀 -> ㅋㅎㅇ
```sql
INSERT INTO APR01_SNACK 
values('오레오', 2500, to_date('2025-04-02 15:00' , 'YYYY-MM-DD HH24:MI'));
SELECT * FROM APR01_SNACK;
-- sysdate : 2025/02/02 11:37:04 라서 오레오 안 뜸
-- 내일 먹으면 죽는 과자
-- 전체 정보
SELECT *
FROM APR01_SNACK
WHERE s_exp <= sysdate; -- X
WHERE s_exp <= 
    to_date(
        concat(
            to_char(
                sysdate, 
                'YYYY-MM-DD'
            ), 
            ' 235959'
        ), 
        'YYYY-MM-DD HH24MISS'
    );
```
- subquery  
    조건에 통계 함수 넣고 싶으면
```sql
-- 국어점수 최고점
-- 이름, 점수
SELECT s_name, s_kor
FROM APR01_STUDENT
WHERE s_kor = (
    SELECT max(s_kor)
    FROM APR01_STUDENT
);
```
- order by  
    기본값은 오름차순  
    desc 붙이면 내림차순
### JOIN
- 테이블 여러개를 붙임
- 모든 경우의 수 별로 다 붙임
```sql
SELECT *
FROM restaurant, menu
WHERE r_no = m_r_no ;
```
- JOIN은 편하지만 모든 경우의 수를 변수로 RAM에 저장하기 때문에 하드웨어적으로 비효율적
- 서브쿼리를 열심히 쓰기 
- distinct : 중복 제거  
    ```SELECT DISTINCT c_name``` 하면 됨
### ?
- =과 in의 차이?  

### Update : UPDATE
```sql
UPDATE 테이블명
SET 필드명=값, 필드명=값, ...
WHERE 조건식;

-- 김씨 사장님네 메뉴 10% 인상
UPDATE APR02_MENU 
SET m_price = m_price * 1.1
WHERE m_r_no in (
	SELECT r_r_no 
	FROM APR02_RUN
	WHERE r_c_no in (
		SELECT c_no
		FROM APR02_CEO
		WHERE c_name LIKE '김%'
	)
);
```
### Delete : DELETE
```sql
DELETE FROM 테이블명
WHERE 조건식;

-- 제일 비싼 메뉴 삭제
DELETE FROM APR02_MENU
WHERE m_price = (
	SELECT max(m_price)
	FROM APR02_MENU
);
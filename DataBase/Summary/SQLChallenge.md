## SQL challenge
### 페이지 나눠서 데이터 가져오기
- sequence는 테이블과 종속되지 않고, 실패해도 카운팅 돼서 여기서 활용할 수 없음
- rownum : select 할 때마다 자동으로 부여되는 가상필드
    - *랑 같이 못 씀
    - order by 보다 먼저 발동됨 ..
    - 이때 subquery 이용
    ```sql
    -- 정렬돼있는 걸 select 하기 가능
    SELECT rownum, m_no, m_name, m_price 
    FROM (
        SELECT m_no, m_name, m_price
        FROM apr02_menu
        ORDER BY m_price desc
    );
    -- 근데 3~5번만 가져오기 위해선 rn을 쓸 수 있게 해야 됨
    SELECT m_no, m_name, m_price
    FROM (SELECT rownum AS rn, m_no, m_name, m_price 
            FROM (
                SELECT m_no, m_name, m_price
                FROM apr02_menu
                ORDER BY m_price desc
            )
    )
    WHERE rn >= 3 AND rn <= 5;
    ```
### 데이터 조회 : R
SELECT 필드명, 필드명 AS 별칭, 연산자, 통계함수, ...
FROM 필드명
WHERE 조건식 
GROUP BY 필드명, 필드명, ... 
HAVING 조건식
ORDER BY 필드명, 필드명 [desc], ...;
- ORDER BY
```sql
-- 카테고리 별 메뉴 평균가
-- 카테고리 별 메뉴 평균가
SELECT m_category, avg(m_price)
FROM apr02_menu
GROUP BY m_category
ORDER BY avg(m_price) desc;
```
- GROUP BY
- HAVING : group by 결과 필터링
    - WHERE : 데이터 필터링

### 외래키
```sql
CREATE TABLE 테이블명(
    ...,
    CONSTRAINT 제약조건명
        FOREIGN KEY(필드명) REFERENCES 테이블명(필드명)
        ON DELETE CASCADE
);
```

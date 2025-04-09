searchTxt = "메롱"
start = 1
end = 2

sql = '''
SELECT s_no, s_name, s_exp, s_price, s_weight, m_name, m_addr, m_ceo, m_employee_num
FROM (
    SELECT s_no, s_name, s_exp, s_price, s_weight, s_c_name
    FROM (
        SELECT rownum AS rn, s_no, s_name, s_exp, s_price, s_weight, s_c_name
        FROM ( '''
sql += '''
        SELECT *
        FROM apr07_snack
        WHERE s_name LIKE '%s'
        ORDER BY s_name, s_price
    )
)
WHERE rn >= %d AND rn <= %d
), (''' % ("%" + searchTxt + "%", start, end)
sql += '''
    SELECT * 
    FROM apr07_manufacturer 
    WHERE m_name IN (
        SELECT s_c_name
        FROM (
            SELECT rownum AS rn, s_no, s_name, s_exp, s_price, s_weight, s_c_name
            FROM (
                SELECT *
                FROM apr07_snack
                WHERE s_name LIKE '%s'
                ORDER BY s_name, s_price
            )
        )
        WHERE rn >= %d AND rn <= %d
    )	
)
WHERE m_name = s_c_name
ORDER BY s_name, s_price
''' % ("%" + searchTxt + "%", start, end)

print(sql)
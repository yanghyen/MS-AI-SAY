from Manufacturer import Manufacturer
from lib.OracleDBManager import OracleDBManager


class ManufacturerDAO:
    def getAll():
        con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
        sql = "select * from apr07_manufacturer order by m_name, m_employee_num"
        cur.execute(sql)
        manufacturers = []
        for name, addr, ceo, emp in cur:
            m = Manufacturer(name, addr, ceo, emp)
            manufacturers.append(m)
        return manufacturers

    def reg(c):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "insert into apr07_manufacturer "
            sql += "values('%s', '%s', '%s', %d)" % (c.name, c.addr, c.ceo, c.emp)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            OracleDBManager.closeConCur(con, cur)

            
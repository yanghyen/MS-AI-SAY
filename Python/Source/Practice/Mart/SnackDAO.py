from lib.OracleDBManager import OracleDBManager
from Snack import Snack


class SnackDAO:
    def getAllSnackCount():
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select count(*) from apr07_snack"
            cur.execute(sql)
            for v in cur:
                print(v[0])
        except:
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def getAll():
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select * from apr07_snack order by s_name, s_price"
            cur.execute(sql)
            snacks = []
            for no, name, exp, price, weight, manufacturerName in cur:
                s = Snack(name, exp, price, weight, manufacturerName)
                snacks.append(s)
            return snacks
        except:
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def reg(s):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "insert into apr07_snack "
            sql += "values(apr07_snack_seq.nextval, '%s', to_date('%s', 'YYYYMMDD'), %d, %d, '%s')" %(s.name, s.exp, s.price, s.weight, s.manufacturerName)
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
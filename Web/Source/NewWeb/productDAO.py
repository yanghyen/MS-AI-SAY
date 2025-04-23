from hyenLib.oracleDBManager import OracleDBManager


class ProductDAO:
    def getAll(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select * from apr23_product"
            cur.execute(sql)

            snacks = []
            for n, p in cur:
                s = {"name":n, "price":p}
                snacks.append(s)
            return snacks
        except Exception as e:
            print(e)
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def reg(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "inser into apr23_product"
            sql += "values('바나나우유', 1300)"
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "등록성공!"
            else:
                return "등록실패ㅠ"
        except Exception as e:
            print(e)
            return "등록 실패 ㅠㅠㅠㅠ"
        finally:
            OracleDBManager.closeConCur(con, cur)
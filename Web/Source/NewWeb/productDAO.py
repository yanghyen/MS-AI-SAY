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

    def reg(self, n, p):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            
            sql = "insert into apr23_product values('%s', '%s')" % (n, p)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result" : n + " 등록 성공"}
            return {"result" : n + " 등록 실패"}
        except:
            return {"result" : n + " 등록 실패"}
        finally:
            OracleDBManager.closeConCur(con, cur)

    def dele(self, m, M):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            
            sql = "delete from apr23_product " 
            sql += "where p_price > %s and p_price < %s" % (m, M)
            cur.execute(sql)

            if cur.rowcount >= 1:
                con.commit()
                return {"result" : "삭제 성공"}
            return {"result" : "삭제 실패"}
        except:
            return {"result" : "삭제 실패"}
        finally:
            OracleDBManager.closeConCur(con, cur)
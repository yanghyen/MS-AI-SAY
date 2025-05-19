from hyenLib.oracleDBManager import OracleDBManager


class SnackDAO:
    def reg(self, name, price):
        try: 
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "insert into may14_snack (s_name, s_price) "
            sql += "values('%s', '%s')" %(name, price)
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

    def get(self):
        try: 
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            
            sql = "select * from may14_snack"
            cur.execute(sql)
            snacks = []
            for name, price in cur:
                s = {
                    "name" : name,
                    "price" : price
                }
                snacks.append(s)
            regResult = {
                "result" : "성공",
                "snacks" : snacks
            }
            return regResult
        except Exception as e:
            print(e)
            return "조회 실패"
        finally:
            OracleDBManager.closeConCur(con, cur)
        
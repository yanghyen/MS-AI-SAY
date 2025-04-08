from math import ceil
from lib.OracleDBManager import OracleDBManager
from Snack import Snack


class SnackDAO:
    def __init__(self):
        self.setAllSnackCount()
        self.snackPerPage = 3
        
    def setAllSnackCount(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select count(*) from apr07_snack"
            cur.execute(sql)
            for v in cur:
                self.allSnackCount = v[0]
        except Exception as e:
            print(e)
        finally:
            OracleDBManager.closeConCur(con, cur)

    def get(self, pageNo, searchTxt):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
          
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.snackPerPage + 1
            end = start * self.snackPerPage 
          
            sql = "SELECT * "
            sql += "FROM (SELECT rownum AS rn, s_no, s_name, s_exp, s_price, s_weight, s_c_name "
            sql += "FROM (select * from apr07_snack " 
            sql += "WHERE s_name like '%s' order by s_name, s_price)) " %("%" + searchTxt + "%")
            sql += "WHERE rn >= %d AND rn <= %d" %(start, end)

            cur.execute(sql)
            # 여기 수정하면 됨!!! snacks에 안 담기는 거
            snacks = []
            for _, no, name, exp, price, weight, manufacturerName in cur:
                s = Snack(name, exp, price, weight, manufacturerName)
                snacks.append(s)
            print(snacks)
            return snacks
        except:
            print(sql)
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def getAll(self):
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

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            snackCount = self.allSnackCount
        else:
            snackCount = self.getSearchSnackCount(searchTxt)
        return ceil(snackCount / self.snackPerPage)
    
    def getSearchSnackCount(self, searchTxt):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            searchTxt = "%" + searchTxt + "%"
            sql = "select count(*) " \
            "from apr07_snack " \
            "where s_name like '%s'" % searchTxt
            cur.execute(sql)
            for v in cur:
                return v[0]
        except Exception as e:
            print(e)
        finally:
            OracleDBManager.closeConCur(con, cur)

    def reg(self, s):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "insert into apr07_snack "
            sql += "values(apr07_snack_seq.nextval, '%s', to_date('%s', 'YYYYMMDD'), %d, %d, '%s')" %(s.name, s.exp, s.price, s.weight, s.manufacturerName)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allSnackCount += 1
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            OracleDBManager.closeConCur(con, cur)

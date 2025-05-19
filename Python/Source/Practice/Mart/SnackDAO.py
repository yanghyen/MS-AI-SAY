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
            snacks = []
            for _, no, name, exp, price, weight, c_name in cur:
                s = Snack(no, name, exp, price, weight, c_name)
                snacks.append(s)
            return snacks
        except:
            print(sql)
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def get2(self, pageNo, searchTxt):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
          
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.snackPerPage + 1
            end = start * self.snackPerPage 

            # join
            # A : 100개
            # B : 100개
            # 1) A, B join하면 10000개로 데이터 폭증
                # 과자만 가져오고, 회사는 Python으로 따로 가져와서
                # 과자가 3개라 치면 
                    # 조회 1    조회 3 -> 총 조회횟수 N+1번이 됨
            # 2) 필요한 것만 가져와서 join

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

            cur.execute(sql)
            # 여기 수정하면 됨!!! snacks에 안 담기는 거
            snacks = []
            for no, name, exp, price, weight, c_name in cur:
                s = Snack(name, exp, price, weight, c_name)
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
            for no, name, exp, price, weight, c_name in cur:
                s = Snack(name, exp, price, weight, c_name)
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
            sql += "values(apr07_snack_seq.nextval, '%s', to_date('%s', 'YYYYMMDD'), %d, %d, '%s')" %(s.name, s.exp, s.price, s.weight, s.c_name)
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

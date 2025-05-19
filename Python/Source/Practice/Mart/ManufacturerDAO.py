from math import ceil
from Manufacturer import Manufacturer
from lib.OracleDBManager import OracleDBManager


class ManufacturerDAO:
    def __init__(self):
        self.manufacturerPerPage = 3
        self.setAllManufacturerCount()

    def setAllManufacturerCount(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select count(*) from apr07_manufacturer"
            cur.execute(sql)
            for v in cur:
                self.allManufacturerCount = v[0]
        except Exception as e:
            print(e)
        finally:
            OracleDBManager.closeConCur(con, cur)

    def get(self, pageNo):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")

            pageNo = int(pageNo)
            start = (pageNo - 1) * self.manufacturerPerPage + 1
            end = start * self.manufacturerPerPage

            sql = "SELECT * " \
            "FROM (SELECT rownum AS rn, m_name, m_addr, m_ceo, m_employee_num " \
            "FROM APR07_MANUFACTURER) " \
            "WHERE rn >= %d AND rn <= %d" %(start, end)

            cur.execute(sql)
            manufacturers = []
            for _, name, addr, ceo, emp in cur:
                m = Manufacturer(name, addr, ceo, emp)
                manufacturers.append(m)
            return manufacturers
        except Exception as e:
            print(e)
        finally:
            OracleDBManager.closeConCur(con, cur)            

    def getAll(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select * from apr07_manufacturer order by m_name, m_employee_num"
            cur.execute(sql)
            manufacturers = []
            for name, addr, ceo, emp in cur:
                m = Manufacturer(name, addr, ceo, emp)
                manufacturers.append(m)
            return manufacturers
        except Exception as e:
            print(e)
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)
    
    def getAllPageCount(self, searchTxt):
        if searchTxt == "":
            manufacturerCount = self.allManufacturerCount
        else:
            manufacturerCount = self.getSearchManufacturerCount(searchTxt)
        return ceil(manufacturerCount / self.manufacturerPerPage)
    
    def getSearchManufacturerCount(self,searchTxt):
        try:
            # DB접속 라이브러리에 있는 연결 함수 사용
            con,cur =OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            searchTxt="%"+searchTxt+"%"
            sql="select count(*) from apr07_manufacturer where c_name like '%s'" % searchTxt
            cur.execute(sql)
            for v in cur:
                # DB 결과가 튜플이라 튜플의 원소 하나만 불러와야 숫자만 제대로 불러와짐. 
                return v[0]
        except:
            return -1
        finally:
            # DB접속 라이브러리에 있는 연결해제 함수 사용
            OracleDBManager.closeConCur(con,cur)


    
    def reg(self, c):
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

            
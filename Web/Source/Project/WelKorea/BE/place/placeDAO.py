from math import ceil
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from hyenLib.oracleDBManager import OracleDBManager


class PlaceDAO:
    def __init__(self):
        self.placePerPage = 10
        self.setAllPlaceCount()

    def get(self):
        try:
            placeCount = self.allPlaceCount
            pageCount = ceil(placeCount / self.placePerPage)
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")

            sql = "select * from may7_places"
            cur.execute(sql)
            places = []
            for no, name_kor, name_eng, translated_name_eng, address, lat, lng, created_at, last_searched_at, desc in cur:
                p = {
                    "no" : no,
                    "name_kor" : name_kor,
                    "name_eng" : name_eng,
                    "translated_name_eng" : translated_name_eng,
                    "address" : address,
                    "lat" : lat,
                    "lng" : lng,
                    "created_at" : created_at.strftime('%Y-%m-%d %H:%M:%S') if last_searched_at else None,  # datetime을 문자열로 변환
                    "last_searched_at" : last_searched_at.strftime('%Y-%m-%d %H:%M:%S') if last_searched_at else None,
                    "desc" : desc
                }
                places.append(p)
                result = {
                    "pageCount" : pageCount,
                    "places" : places
                }
            return result
        except Exception as e:
            print(e)
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def getDetail(self, no):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")

            sql = '''SELECT * FROM may7_places WHERE p_no = %s''' % no
            
            cur.execute(sql)
            for no, name_kor, name_eng, translated_name_eng, address, lat, lng, created_at, last_searched_at, desc in cur:
                p = {
                    "no" : no,
                    "name_kor" : name_kor,
                    "name_eng" : name_eng,
                    "translated_name_eng" : translated_name_eng,
                    "address" : address,
                    "lat" : lat,
                    "lng" : lng,
                    "created_at" : created_at.strftime('%Y-%m-%d %H:%M:%S') if last_searched_at else None,  # datetime을 문자열로 변환
                    "last_searched_at" : last_searched_at.strftime('%Y-%m-%d %H:%M:%S') if last_searched_at else None,
                    "desc" : desc
                }
                return p
        except Exception as e:
            print(e)
            return {"result" : "조회 실패"}
        finally:
            OracleDBManager.closeConCur(con, cur)
            
    def reg(self, name, desc):
        try: 
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "insert into may7_places (p_no, p_name_eng, p_desc) "
            sql += "values(may7_places_seq.nextval, '%s', '%s')" %(name, desc)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            return "등록 실패"
        finally:
            OracleDBManager.closeConCur(con, cur)

    def setAllPlaceCount(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select count(*) from may7_places "
            cur.execute(sql)
            for c in cur:
                self.allPlaceCount = c[0]
        except:
            pass
        finally:
            OracleDBManager.closeConCur(con, cur)
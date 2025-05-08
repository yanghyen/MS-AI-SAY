from typing import final
from place import Place
from hyenLib.oracleDBManager import OracleDBManager


class PlaceDAO:
    def get(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")

            sql = "select * from may7_places"
            cur.execute(sql)
            places = []
            for no, name_kor, name_eng, translated_name_eng, address, lat, lng, created_at, last_searched_at in cur:
                p = {
                    "no" : no,
                    "name_kor" : name_kor,
                    "name_eng" : name_eng,
                    "translated_name_eng" : translated_name_eng,
                    "address" : address,
                    "lat" : lat,
                    "lng" : lng,
                    "created_at" : created_at,
                    "last_searched_at" : last_searched_at
                }
                places.append(p)
                # result = {
                #     "pageCount" : pageCount,
                #     "places" : places
                # }
            print(places)
            return places
        except Exception as e:
            print(e)
            return None
        finally:
            OracleDBManager.closeConCur(con, cur)

    def reg(self, nn, ee, aa):
        try: 
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "insert into may7_places "
            sql += "values(may7_places_seq.nextval, '%s', '%s', '%s')" %(nn, ee, aa)
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
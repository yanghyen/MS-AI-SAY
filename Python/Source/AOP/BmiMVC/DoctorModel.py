from oracledb import connect

from lib.OracleDBManager import OracleDBManager


class Doctor:
    def calculate(guest):
        con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")

        h = guest.height / 100
        guest.bmi = guest.weight / h**2

        if (guest.bmi >= 39):
            guest.result = "고도 비만"
        elif(30 <= guest.bmi < 39):
            guest.result = "비만"
        elif(24 <= guest.bmi < 30):
            guest.result = "과체중"
        elif(10 <= guest.bmi < 24):
            guest.result = "정상"
        else:
            guest.result = "저체중"

        sql = "insert into apr07_bmi"
        sql += " values('%s', %.2f, %.2f, %.2f, '%s')" % (guest.name, guest.height, guest.weight, guest.bmi, guest.result)

        cur.execute(sql)
        if cur.rowcount == 1:
            print("추가 성공!")
            con.commit()

        OracleDBManager.closeConCur(con, cur)
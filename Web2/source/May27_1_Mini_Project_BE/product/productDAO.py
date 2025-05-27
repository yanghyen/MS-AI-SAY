from logging import Logger
from typing import final

from fastapi.logger import logger
from fastapi.responses import FileResponse

from hyenLib.ImageManager import ImageManager
from hyenLib.oracleDBManager import OracleDBManager


class ProductDAO:
    def __init__(self):
        self.folder = './product/img/'
        
    async def reg(self, name, price, desc, image):
        try:
            content = await image.read()
            if len(content) > 20 * 1024 * 1024:
                raise Exception("파일 크기 초과")   # 강제로 Exception 발생
            fileName = image.filename
            fileName = ImageManager.generate(fileName, "date")
            f = open(self.folder + fileName, "wb")
            f.write(content)
            f.close()
        except:
            logger.error(f"파일 저장 실패: {e}")
            return {"result":"등록 실패(파일)"}

        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            print("연결성공")
            
            sql = "insert into may27_product (p_name, p_price, p_desc, p_image) values (:1, :2, :3, :4)"
            cur.execute(sql, (name, price, desc, fileName))

            if cur.rowcount == 1:
                con.commit()
                return {"result":"등록 성공"}
            else:
                return {"result":"등록 실패1(DB)"}
        except Exception as e:
            print("등록 실패2(DB) 에러 발생")  # 우선 이 문장만 출력 확인
            print(f"에러 메시지: {e}")
            return {"result":"등록 실패2(DB)"}
        finally:
            OracleDBManager.closeConCur(con, cur)

    def get(self):
        try:
            con, cur = OracleDBManager.makeConCur("yanghyen/0317@195.168.9.126:1521/xe")
            sql = "select * from may27_product"
            cur.execute(sql)
            products = []
            for row in cur:
                p = {
                    "name" : row[0],
                    "price" : row[1],
                    "desc" : row[2],
                    "image" : row[3]
                }
                products.append(p)
                result = {
                    "result" : "조회성공",
                    "products" : products
                }
            return result
        except Exception as e:
            print(e)
            return {"result" : "조회실패"}
        finally:
            OracleDBManager.closeConCur(con, cur)

    def getImg(self, image):
        return FileResponse(self.folder + image, filename=image)
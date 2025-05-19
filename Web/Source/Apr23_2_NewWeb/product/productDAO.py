from kwon.kwonDBManager import KwonDBManager

class ProductDAO:
    def getAll(self):
        try:
            con, cur = KwonDBManager.makeConCur(
                "kwon/1@195.168.9.214:1521/xe"
            )

            sql = "select * from apr23_product order by p_name"
            cur.execute(sql)

            products = []
            for n, p in cur:
                products.append({"name": n, "price": p})
            return products
        except:
            return None
        finally:
            KwonDBManager.closeConCur(con, cur)

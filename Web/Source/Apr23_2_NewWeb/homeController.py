from fastapi import FastAPI
from fastapi.responses import JSONResponse
from product.productDAO import ProductDAO

app = FastAPI()
pDAO = ProductDAO()

@app.get("/product.get")
def productGet():
    resBody = pDAO.getAll()
    resHeader = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(resBody, headers=resHeader)

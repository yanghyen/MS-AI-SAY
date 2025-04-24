from fastapi import FastAPI
from fastapi.responses import JSONResponse
from requests import head

from productDAO import ProductDAO



app = FastAPI()
pDAO = ProductDAO()

@app.get("/product.get")
def snackGet():
    resBody = pDAO.getAll()
    resHeader = {"Access-Controller-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/product.reg")
def productReg(namee, pricee):
    resBody = pDAO.reg(namee, pricee)
    resHeader = {"Access-Controller-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/product.dele")
def productDele(minn, maxx):
    resBody = pDAO.dele(minn, maxx)
    resHeader = {"Access-Controller-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)
# socket port : 52555
# FastAPI port : 3344

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from snackDAO import SnackDAO


app = FastAPI()
sDAO = SnackDAO()

@app.get("/snack.reg")
def snackReg(name:str, price:int):
    resBody = sDAO.reg(name, price)
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/snack.get")
def snackGet():
    resBody = sDAO.get()
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)
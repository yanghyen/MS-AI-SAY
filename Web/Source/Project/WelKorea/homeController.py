from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

from BE.place.placeDAO import PlaceDAO


app = FastAPI()
pDAO = PlaceDAO()

# 이 /place.get은 조회해보려고 대충 만든거임
@app.get("/place100.get")
def placeGet():
    resBody = pDAO.get()
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/place100.get.detail")
def placeGetDetail(no):
    resBody = pDAO.getDetail(no)
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)

@app.get("/place100.reg")
def placeReg(name: str, desc: str):
    resBody = pDAO.reg(name, desc)
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

from placeDAO import PlaceDAO


app = FastAPI()
pDAO = PlaceDAO()

@app.get("/place.get")
def placeGet():
    resBody = pDAO.get()
    resHeader = {"Access-Controller-Allow-Origin" : "*"}
    return Response(resBody, headers=resHeader)

@app.get("/place.reg")
def placeReg(name_kor, name_eng, addr):
    resBody = pDAO.reg(name_kor, name_eng, addr)
    resHeader = {"Access-Controller-Allow-Origin" : "*"}
    return JSONResponse(resBody, headers=resHeader)
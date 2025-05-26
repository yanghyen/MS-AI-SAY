from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse

from photo.photoManager import PhotoManager
from calculator.calculator import Calculator



app = FastAPI()
pm = PhotoManager()

@app.get("/calculator.get")
def calculatorGet(x, y):
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(Calculator.calculate(x, y), headers=h)

@app.post("/calculator.post")
async def calculatorPost(x:int=Form(), y:int=Form()):
    h = {
        "Access-Control-Allow-Origin": "http://localhost:3000", 
         "Access-Control-Allow-Credentials":"true"  # 위에 주소 정확히 써야 됨
        }
    return JSONResponse(Calculator.calculate(x, y), headers=h)

@app.post("/photo.upload")
async def photoUpload(photo:UploadFile, title:str=Form()):
    r = await pm.upload(photo, title)
    h = {
        "Access-Control-Allow-Origin": "http://localhost:3000", 
         "Access-Control-Allow-Credentials":"true"  # 위에 주소 정확히 써야 됨
        }
    return JSONResponse(r, headers=h)

@app.post("/photo.get")
async def photoGet(photo):
    return pm.getFile(photo)
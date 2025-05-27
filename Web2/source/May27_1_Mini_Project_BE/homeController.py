from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

from product.productDAO import ProductDAO

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

app = FastAPI()
pDAO = ProductDAO()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 필요한 origin 모두 적기
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/te.st")
def test():
    return {"C":"B"}

@app.post("/product.reg")
async def productReg(image: UploadFile, name: str = Form(), price: int = Form(), desc: str = Form()):
    try:
        resBody = await pDAO.reg(name, price, desc, image)
        return JSONResponse(resBody)
    except Exception as e:
        print(f"Error in productReg: {e}")
        return JSONResponse({"result": "서버 에러 발생"}, status_code=500)

@app.post("/product.get")
def productGet():
    resBody = pDAO.get()
    h = {
        "Access-Control-Allow-Origin": "http://localhost:3000", 
         "Access-Control-Allow-Credentials":"true"  # 위에 주소 정확히 써야 됨
        }
    return JSONResponse(resBody, headers=h)

@app.get("/product.get.img")
def productImgGet(image):
    return pDAO.getImg(image)
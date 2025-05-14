# socket port : 52555
# FastAPI port : 3299

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from snackDAO import SnackDAO


app = FastAPI()
sDAO = SnackDAO()

@app.reg("/snack.reg")
def snackGet():
    resBody = sDAO.reg()
    resHeader = {"Access-Control-Allow-Origin", "*"}
    return JSONResponse(resBody, headers=resHeader)
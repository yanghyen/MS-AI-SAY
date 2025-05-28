from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from menu.menuManager import MenuManager


app = FastAPI()
mm = MenuManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/menu.reg")
def menuReg(name, price):
    m = mm.reg(name, price)
    return m

@app.get("/menu.get")
def menuGet(token):
    return mm.get(token)

@app.get("/menu.update")
def menuUpdate(token):
    return mm.update(token)
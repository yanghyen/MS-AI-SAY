from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.post("/member.sign.up")
def memberSignUp(id:str=Form(), pw:str=Form()):
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>%s</h1>" % id
    html += "<h1>%s</h1>" % pw
    html += "</body></html>"
    return HTMLResponse(html)
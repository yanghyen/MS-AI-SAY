from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.post("/member.sign.up")
def memberSignUp(id:str=Form(), pw:str=Form(),
                 gender:str=Form(), addr:str=Form(), ability:Optional[list[str]]=Form(None),
                 comment:str=Form()):
    comment = comment.replace("\r\n", "<br>")
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>소속 : %s</h1>" % id
    html += "<h1>번호 : %s</h1>" % pw
    html += "<h1>종족 : %s</h1>" % gender
    html += "<h1>주소 : %s</h1>" % addr
    if ability != None:
        html += "<h1>악마의 열매 : </h1>" % ability
        for a in ability:
            html += "<h1>%s</h1>" % a
    html += "<h1>할 말 : <br>%s</hq>" % comment
    html += "</body></html>"
    return HTMLResponse(html)
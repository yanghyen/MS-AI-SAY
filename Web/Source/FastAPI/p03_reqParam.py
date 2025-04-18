from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/calculate.do")
def calculate_do(xxx:int, yyy:int): # param변수명:자료형
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += '<table border="1">'
    html += "<tr><td>%d + %d = %d </td></tr>" %(xxx , yyy, xxx + yyy)
    html += "<tr><td>%d - %d = %d </td></tr>" %(xxx , yyy, xxx - yyy)
    html += "<tr><td>%d * %d = %d </td></tr>" %(xxx , yyy, xxx * yyy)
    html += "<tr><td>%d / %d = %d </td></tr>" %(xxx , yyy, xxx / yyy)
    html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)

@app.post("/gugudan.show")
def gugudan_show(start:int=Form(), end:int=Form()): # param변수명:자료형=Form()
    html = "<html><head><meta charset\"utf-8\"></head><body>"
    for i in range(start, end+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<th>%d단</th>" %i
        for j in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" %(i, j, i * j)
        html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)
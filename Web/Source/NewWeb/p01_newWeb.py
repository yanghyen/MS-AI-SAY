from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse


app = FastAPI()

@app.get("/te.st")
def test():
    html = "<html><head><meta charset=\"utf-8\"></head></html>"
    html += "<h1>hi</h1>"
    return HTMLResponse(html)

@app.get("/xml.test")
def xmlTest():
    xmll = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    xmll += "<snacks>"
    xmll += "<snack>"
    xmll += "<s_name>촉촉한초코칩</s_name>"
    xmll += "<s_price>2000</s_price>"
    xmll += "</snack>"
    xmll += "<snack>"
    xmll += "<s_name>다이제</s_name>"
    xmll += "<s_price>3000</s_price>"
    xmll += "</snack>"
    xmll += "</snacks>"
    h = {"Access-Control-Allow-Origin" : "*"}
    return Response(xmll, media_type="application/xml", headers=h)

@app.get("/json.test")
def jsonTest():
    jsonn = [
        {"s_name" : "촉촉한초코칩", "s_price" : 2000},
        {"s_name" : "다이제", "s_price" : 3000}
    ]
    # 결과를 외부에서도 사용 가능하게 하려면
    # Access-Control-Allow-Origin이라는 응답헤더 세팅돼야 함
    # h = {"Access-Control-Allow-Origin" : "IP주소"}
    h = {"Access-Control-Allow-Origin" : "*"}

    return JSONResponse(jsonn, headers=h)
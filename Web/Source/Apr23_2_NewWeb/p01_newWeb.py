from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

# 클래식웹 :
#   back-end(FastAPI) : 7
#       프로그램스러운 작업 다 해서 -> 서버쪽 부담
#       HTML+CSS+JS 완성시켜서 응답 -> 작업불편
#   front-end(JavaScript) : 3
#       완성된 웹사이트에 효과 부여
# 신형웹 :
#   back-end(FastAPI) : 3
#       DB관련 작업만, 결과를 front-end쪽에서 쓸수있게(XML/JSON으로 응답)
#   front-end(JavaScript) : 7
#       프로그램스러운 작업 다 하자
#       DB관련 작업은 back-end쪽 통해서(AJAX(XML/JSON파싱))

@app.get("/xml.test")
def xmlTest():
    xmll = '<?xml version="1.0" encoding="UTF-8"?>'
    xmll += "<snacks>"
    xmll += "<snack>"
    xmll += "<s_name>빼빼로</s_name>"
    xmll += "<s_price>2000</s_price>"
    xmll += "</snack>"
    xmll += "<snack>"
    xmll += "<s_name>새우깡</s_name>"
    xmll += "<s_price>3000</s_price>"
    xmll += "</snack>"
    xmll += "</snacks>"
    h = {"Access-Control-Allow-Origin" : "*"}
    return Response(xmll, media_type="application/xml", headers=h)


@app.get("/json.test")
def jsonTest():
    jsonn = [
        {"s_name": "빼빼로", "s_price": 2000},
        {"s_name": "새우깡", "s_price": 3000},
    ]
    # 결과를 외부에서도 사용 가능하게 하려면
    # Access-Control-Allow-Origin이라는 응답헤더를 세팅
    h = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(jsonn, headers=h)

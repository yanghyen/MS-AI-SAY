from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI()

@app.post("/bmi.check")
async def bmiCheck(photo:UploadFile, name:str=Form(), height:float=Form(), weight:float=Form()):
    folder = './photo/'
    content = await photo.read()    # 파일 내용 다 불러오면 
    fileName = photo.filename
    type = fileName[-4:]    # .png
    fileName = fileName.replace(type, "")
    fileName = fileName + str(uuid4()) + type
    print(fileName, type)

    f = open(folder + fileName, "wb")
    f.write(content)
    f.close()

    h = height / 100
    bmi = weight / (h * h)
    result = "메롱"
    if bmi >= 39:
        result = "고도비만"
    elif bmi >= 32:
        result = "중도비만"

    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>결과</h1>"
    html += "<img src=\"file.get?fname=%s\">" % fileName
    html += "<h2>이름 : %s</h2>" % name
    html += "<h2>키 : %.1f</h2>" % height
    html += "<h2>몸무게 : %.1f</h2>" % weight
    html += "<h2>BMI : %.1f</h2>" % bmi
    html += "<h2>결과 : %s</h2>" % result 
    html += "</body></html>"
    return HTMLResponse(html)

# ~~/file.get/fname=새capybara.png
# html에 <img src=\"file.get?..."에 써둠
@app.get("/file.get")
async def fileGet(fname):
    folder = './photo/'
    return FileResponse(folder + fname, filename=fname)
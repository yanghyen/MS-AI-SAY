from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse


app = FastAPI()

@app.post("/file.up")
async def test(photo:UploadFile, title:str=Form()):
    folder = './image/'
    content = await photo.read()    # 파일 내용 다 불러오면 
    fileName = photo.filename
    type = fileName[-4:]    # .png
    fileName = fileName.replace(type, "")
    fileName = fileName + str(uuid4()) + type
    print(fileName, type)

    f = open(folder + fileName, "wb")
    f.write(content)
    f.close()

    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>제목 : %s</h1>" % title
    html += "<img src=\"file.get?fname=%s\">" % fileName
    html += "</body></html>"
    return HTMLResponse(html)

# ~~/file.get/fname=새capybara.png
@app.get("/file.get")
async def fileGet(fname):
    folder = './image/'
    return FileResponse(folder + fname, filename=fname)
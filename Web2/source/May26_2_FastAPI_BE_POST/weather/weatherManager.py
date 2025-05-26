from datetime import datetime
from fastapi.responses import FileResponse, JSONResponse


class WeatherManager:
    def __init__(self):
        self.imageFolder = "./weather/image/"

    def getIcon(self, icon):
        return FileResponse(self.imageFolder + icon, filename=icon)

    async def reg(self, icon, desc, temp):
        now = datetime.today()
        now = datetime.strftime(now, "%Y%m%d%H%M%S")

        content = await icon.read()
        fileName = icon.filename
        type = fileName[-4:]
        fileName = fileName.replace(type, "")
        fileName += "_" + now + type

        f = open(self.imageFolder + fileName, "wb")
        f.write(content)
        f.close()

        r = {"result":"성공", "desc":desc, "temp":temp, "icon":fileName}
        h = {
        "Access-Control-Allow-Origin": "http://localhost:3000", 
        "Access-Control-Allow-Credentials":"true"  # 위에 주소 정확히 써야 됨
        }  
        return JSONResponse(r, headers=h)
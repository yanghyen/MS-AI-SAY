from datetime import datetime
from uuid import uuid4

from fastapi.responses import FileResponse


class ImageManager:
    def generate(fileName, mode):
        type = fileName[-4:]
        fileName = fileName.replace(type, "")

        if mode == "uudi":
            uuid = str(uuid4())
            return fileName + "_" + uuid + type
        elif mode == "date":
            now = datetime.today()
            now = datetime.strftime(now, "%Y%m%d%H%M%S")
            return fileName + "_" + now + type
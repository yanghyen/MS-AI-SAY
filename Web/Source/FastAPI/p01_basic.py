from fastapi import FastAPI


app = FastAPI()

@app.get("/te.st")
def test():
    d = {"name" : "힝", "price" : 499}
    return d
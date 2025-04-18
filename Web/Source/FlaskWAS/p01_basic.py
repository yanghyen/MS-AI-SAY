from flask import Flask


app = Flask(__name__)

@app.get("/te.st")       # /test 주소로 클라이언트에게 GET방식 요청 받으면
def test():             # 이 함수 자동 실행
    print("aaa")
    return "adbs"

if __name__ == "__main__":
    app.run(
        "0.0.0.0",
        1234,
        debug=True
    )
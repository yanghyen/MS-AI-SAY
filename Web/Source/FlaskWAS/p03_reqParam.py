from flask import Flask, request


app = Flask(__name__)

@app.get("/html.test")
def html_test():
    html = "<html><head><meta charset\"utf-8\"></head><body>"
    html += "<marquee>ㅋㅋㅋ</marquee>"
    html += "</body></html>"
    return html

# http://IP주소:port/calculate.do?xxx=값&yyy=값
@app.get("/calculate.do")
def calculate_do():
    x = int(request.args.get("xxx"))    # request.args.get("reqParam 변수명") -> str
    y = int(request.args.get("yyy"))
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<table border=\"1\">"
    html += "<tr><td>%d + %d = %d </td></tr>" %(x , y, x + y)
    html += "<tr><td>%d - %d = %d </td></tr>" %(x , y, x - y)
    html += "<tr><td>%d * %d = %d </td></tr>" %(x , y, x * y)
    html += "<tr><td>%d / %d = %d </td></tr>" %(x , y, x / y)
    html += "</table>"
    html += "</body></html>"
    return html

# http://IP:port/gugudan.show
@app.post("/gugudan.show")
def gugudan_show():
    s = int(request.form["start"])    
    e = int(request.form["end"])    
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    for i in range(s, e+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<th>%d단</th>" %i
        for j in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" %(i, j, i * j)
        html += "</table>"
    html += "</body></html>"
    return html















if __name__ == "__main__":
    app.run(
        "0.0.0.0",
        1234,
        debug=True
    )
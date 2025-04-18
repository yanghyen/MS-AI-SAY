from flask import Flask


app = Flask(__name__)

@app.get("/xy.calculate")
def getCalculate():
    a = 10
    b = 10
    c = a + b
    html = "<html><head><meta charset\"utf-8\"></head><body>"
    html += "<h1>%d</h1>" % c
    html += "</body></html>"
    return html


@app.get("/gugudan.show")
def gugudan():
    html = "<html><head><meta charset\"utf-8\"></head><body>"
    for i in range(2, 10):
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
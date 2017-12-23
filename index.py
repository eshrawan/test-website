from flask import Response, Flask, request, current_app as app
import os
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def homePage():
    return app.send_static_file('index.html')

@app.route("/form")
def formPage():
    return app.send_static_file('form.html')

@app.route("/submit", methods=["POST"])
def submitPage():
    a = request.args.post('fvalue')
    b = request.args.post('svalue')
    c = request.args.post('tvalue')
    d = request.args.post('fovalue')
    e = request.args.post('fivalue')
    number = [int(a),int(b),int(c),int(d),int(e)]
    numberlen = len(number)
    for k in range(numberlen-1, 0 ,-1):
        for i in range (k):
            if(number[i+1]< number[i]):
                number[i],number[i+1] = number[i+1],number[i]
    return str(number)
    return app.send_static_file('result.html')

@app.route("/add", methods=["GET","POST"])
def addPage():
    a = request.args.get('A')
    b = request.args.get('B')
    return str(int(a)+int(b))

@app.route("/subtract", methods=["GET","POST"])
def subtractPage():
    a = request.args.get('A')
    b = request.args.get('B')
    return str(int(a)-int(b))

@app.route("/multiply", methods=["GET","POST"])
def multiplyPage():
    a = request.args.get('A')
    b = request.args.get('B')
    return str(int(a)*int(b))

@app.route("/divide", methods=["GET","POST"])
def dividePage():
    a = request.args.get('A')
    b = request.args.get('B')
    return str((int(a)/float(b)))

@app.route("/bubblesort", methods=["GET","POST"])
def bubblePage():
    a = request.args.get('A')
    b = request.args.get('B')
    c = request.args.get('C')
    d = request.args.get('D')
    e = request.args.get('E')
    number = [int(a),int(b),int(c),int(d),int(e)]
    numberlen = len(number)
    for k in range(numberlen-1, 0 ,-1):
        for i in range (k):
            if(number[i+1]< number[i]):
                number[i],number[i+1] = number[i+1],number[i]
    return str(number)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port=port, debug =True)


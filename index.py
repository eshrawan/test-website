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
    a = request.form.get('fvalue')
    try:
        value=int(a)
    except ValueError:
        return("The first value is not a number.")
    b = request.form.get('svalue')
    try:
        value=int(b)
    except ValueError:
        return("The second value is not a number.")
    c = request.form.get('tvalue')
    try:
        value=int(c)
    except ValueError:
        return("The third value is not a number.")
    d = request.form.get('fovalue')
    try:
        value=int(d)
    except ValueError:
        return("The fourth value is not a number.")
    e = request.form.get('fivalue')
    try:
        value=int(e)
    except ValueError:
        return("The fifth value is not a number.")
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


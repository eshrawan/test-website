from flask import Response, Flask, request, current_app as app
import os
app = Flask(__name__)

@app.route("/")
def homePage():
    return "Hello User"

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
    a= request.args.get('A')
    b = request.args.get('B')
    c = request.args.get('C')
    d = request.args.get('D')
    e = request.args.get('E')
    number = [a,b,c,d,e]
    numberlen = len(number)
    for k in range(numberlen-1, 0 ,-1):
        for i in range (k):
            if(number[i+1]< number[i]):
                number[i],number[i+1] = number[i+1],number[i]
    print(number)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port, debug = True)

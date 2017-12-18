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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port, debug = True)

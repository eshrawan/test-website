from flask import Response, Flask, request, current_app as app
import os
app = Flask(__name__)

@app.route("/")
def indexPage():
    return "Hello"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port, debug = True)

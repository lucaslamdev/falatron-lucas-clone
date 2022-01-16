import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste")
def hello_world():
    return "<p>Hello, teste!</p>"

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)

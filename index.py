from flask import Flask
import os

porta = os.environ.get('PORT', 8000)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
  
app.run(host='0.0.0.0', port=porta)

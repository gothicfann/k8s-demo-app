import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return os.environ['VERSION']

app.run(host='0.0.0.0')

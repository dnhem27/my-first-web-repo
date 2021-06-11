from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "Hello World! This is my first Python web app."

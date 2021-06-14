from flask import Flask, render_template

my_hello_world_webapp = Flask(__name__)


@my_hello_world_webapp.route('/')
@my_hello_world_webapp.route('/home')
def home():
    return render_template('index.html')

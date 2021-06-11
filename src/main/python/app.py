from flask import Flask

my_hello_world_webapp = Flask(__name__)


@my_hello_world_webapp.route('/')
@my_hello_world_webapp.route('/home')
def home():
    return "Hello World! This is my first Python web myapp."

from flask import Flask

#add a new flask app instance
# **research "magic method", underscores before and after varible in function
app = Flask(__name__)

# define starting point (root)
#forward slash says put data at the root of the route == highest level of hierarchy
@app.route('/')
def hello_world():
    return 'Hello world'
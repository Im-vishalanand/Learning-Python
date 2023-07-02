from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/greet/<username>')
def greet():
    return 'Welcome'+username

@app.route('/farewell/<username>')
def farewell():
    return 'Welcome'+username




if __name__ == '__main__':
    app.run()
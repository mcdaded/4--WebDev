"""

Flask Tutorial from the Web Development with Flask book.

This is the first Hello World app from flask. to run simply navigate to folder
and enter python hello.py runserver


"""

from flask import Flask, make_response, redirect, abort, request
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'


@app.route('/fun')
def index():
    user_agent = request.headers.get('User-Agent')
    response = make_response('<h1>This document carries a cookie!</h1>' + \
                             '<p>Your browser is %s</p>' % user_agent)
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/redirect')
def appredir():
    return redirect('http://www.example.com')


@app.route('/userid/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name


if __name__ == '__main__':
    manager.run()

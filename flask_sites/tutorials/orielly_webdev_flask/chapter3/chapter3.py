"""

Webdev book Chapter 3 - '' created on 2/5/2018 at 8:54 am

@author: dmcdade

"""

from flask import Flask, render_template
from flask.ext.moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index2():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

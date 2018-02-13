"""
danmcdade_flask - 'main/errors' created on 2/1/2018 at 5:17 PM

@author: dmcdade
"""

from flask import Flask, render_template
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
bootstrap = Bootstrap()
bootstrap.init_app(app)
moment = Moment()
moment.init_app(app)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')


# @app.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
#
# @app.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
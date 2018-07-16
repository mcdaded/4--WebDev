from flask import Flask, render_template
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)

bootstrap = Bootstrap()
moment = Moment()

bootstrap.init_app(app)
moment.init_app(app)

manager = Manager(app)


@app.route("/")
def index():
    return render_template('post_flask.html')


if __name__ == '__main__':
    manager.run()  # command line option for --host=0.0.0.0 --port=5000

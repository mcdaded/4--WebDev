"""

Webdev book Chapter 3 - '' created on 2/5/2018 at 8:54 am

@author: dmcdade

"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

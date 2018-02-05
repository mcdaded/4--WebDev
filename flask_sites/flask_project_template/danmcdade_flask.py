"""
danmcdade_flask - 'manage.py' created on 2/1/2018 at 5:17 PM

@author: dmcdade

#!/usr/bin/env python

"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

"""
Created on Superbowl Sunday February 4th, 2018 at 2:51 pm EST.

@author: dmcdade

This file represents work done while learning Flask web framework.
Follows along from the ORielly Flask Web Development book.

"""


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

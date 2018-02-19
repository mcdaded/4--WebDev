"""
danmcdade_flask - 'main/views' created on 2/1/2018 at 5:17 PM

@author: dmcdade
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .. import db


# Views
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/js', methods=['GET', 'POST'])
def testjs():
    return render_template('testjs.html')


@main.route('/counter', methods=['GET', 'POST'])
def testcounter():
    return render_template('counterjs.html')

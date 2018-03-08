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


@main.route('/greetings', methods=['GET', 'POST'])
def greetingsjs():
    return render_template('greetingsjs.html')


@main.route('/counter', methods=['GET', 'POST'])
def counterjs():
    return render_template('counterjs.html')


@main.route('/tic_tac_toe', methods=['GET', 'POST'])
def tictactoejs():
    return render_template('tic_tac_toe.html')

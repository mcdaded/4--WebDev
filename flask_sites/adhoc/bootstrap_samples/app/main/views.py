from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import main
from .. import db


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/hello', methods=['GET'])
def hello():
    return render_template('hello.html')

@main.route('/post', methods=['GET'])
def post():
    return render_template('post.html')

@main.route('/post2', methods=['GET'])
def post2():
    return render_template('post2.html')

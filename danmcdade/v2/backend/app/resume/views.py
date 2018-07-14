from flask import render_template
from . import resume
from .. import db


@resume.route('/', methods=['GET', 'POST'])
def index():
    return render_template('resume/index.html')

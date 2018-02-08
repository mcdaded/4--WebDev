"""
danmcdade_flask - 'app/main/__init__' created on 2/1/2018 at 5:17 PM

@author: dmcdade

"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


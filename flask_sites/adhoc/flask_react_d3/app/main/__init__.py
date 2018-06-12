"""
Flask+React+D3 - 'app/main/__init__' created on 2/17/2018 at 11:33 AM

@author: dmcdade

"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views

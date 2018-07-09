from flask import jsonify, request, current_app, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from . import admin
from .. import db
from ..models import User, Post

app_admin = Admin(admin, name='admin', url_prefix='/admin', endpoint='admin')
app_admin.add_view(ModelView(User, db.session))
app_admin.add_view(ModelView(Post, db.session))

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from . import admin
from .. import db
from ..models import User, Post
from flask.ext.admin import BaseView, expose, ModelView


class AdminView(BaseView):

    @expose('/')
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('admin/second_page.html')


class AdminModelView(ModelView):
    """ Model view for Flask models """
    pass

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from .. import db
from ..models import User, Post


class AdminIndex(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You do not have access to that page')
        return redirect(url_for('auth.unconfirmed'))


class AdminView(BaseView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You do not have access to that page')
        return redirect(url_for('auth.unconfirmed'))


class AdminModelView(ModelView):
    """ Model view for Flask models """
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You do not have access to that page')
        return redirect(url_for('auth.unconfirmed'))

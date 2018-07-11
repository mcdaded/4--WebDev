from flask_login import login_user, logout_user, login_required, current_user
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from .. import db
from ..models import User, Post


class AdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


class AdminModelView(ModelView):
    """ Model view for Flask models """
    def is_accessible(self):
        return current_user.is_authenticated

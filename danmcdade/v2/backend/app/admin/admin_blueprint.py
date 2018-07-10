from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class AdminBlueprint(Blueprint):
    views=None

    def __init__(self,*args, **kargs):
        self.views = []
        # return super(AdminBlueprint, self).__init__('admin_blueprint', __name__, url_prefix='/admin', static_folder='static', static_url_path='/static/admin')
        return super(AdminBlueprint, self).__init__('admin_blueprint', __name__, url_prefix='/admin')

    def add_view(self, view):
        self.views.append(view)

    def register(self, app, options, first_registration=False):
        print(app)
        admin = Admin(app, name='admin')
        # admin = Admin(app, name='admin_site', template_mode='adminlte')
        for v in self.views:
            admin.add_view(v)

        return super(AdminBlueprint, self).register(app, options, first_registration)

import flask_admin
from ..models import User, Post, db
from .admin_blueprint import AdminBlueprint
from .views import AdminModelView

# admin = AdminBlueprint('admin', __name__, url_prefix='/admin', static_folder='static', static_url_path='/static/admin')
admin = AdminBlueprint('admin', __name__)
admin.add_view(AdminModelView(User, db.session))

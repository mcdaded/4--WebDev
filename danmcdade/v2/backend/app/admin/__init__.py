import flask_admin
from ..models import User, Post, db
from .admin_blueprint import AdminBlueprint
from .views import AdminModelView, AdminView

# admin = AdminBlueprint('admin', __name__, url_prefix='/admin', static_folder='static', static_url_path='/static/admin')
admin = AdminBlueprint('admin', __name__)

admin.add_view(AdminView(name='AdminPage'))

db_post_models = [User, Post]
for db_model in db_post_models:
    admin.add_view(AdminModelView(db_model, db.session, category='Blog'))

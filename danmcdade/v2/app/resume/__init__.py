from flask import Blueprint

resume = Blueprint('resume', __name__)

from . import views
from ..models import Permission


@resume.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

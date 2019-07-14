from flask import Blueprint

menu_items = Blueprint('menu_items', __name__)

from . import views

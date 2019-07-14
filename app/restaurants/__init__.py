from flask import Blueprint

restaurants = Blueprint('restaurants', __name__)

from . import views

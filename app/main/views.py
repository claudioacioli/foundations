from flask import render_template
from . import main
from .. import db
from ..models import Restaurant, MenuItem


@main.route('/restaurants/')
@main.route('/')
def show_restaurants():
    restaurants = db.session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@main.route('/restaurants/<int:restaurant_id>/')
@main.route('/restaurants/<int:restaurant_id>/menu/')
def show_menu(restaurant_id):
    menu_items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menus.html', menu_items=menu_items)
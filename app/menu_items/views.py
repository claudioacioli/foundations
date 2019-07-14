from flask import render_template
from .. import db
from ..models import MenuItem
from . import menu_items as app_menu_items


@app_menu_items.route('/')
def show_menu(restaurant_id):
    menu_items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menus.html', menu_items=menu_items)
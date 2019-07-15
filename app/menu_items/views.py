from flask import render_template, request
from .. import db
from .forms import CreateMenuItem
from ..models import MenuItem
from . import menu_items as app_menu_items


@app_menu_items.route('/')
def show_menu(restaurant_id):
    menu_items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menus.html', menu_items=menu_items, restaurant_id=restaurant_id)


@app_menu_items.route('/new', methods=['GET'])
def create_menu(restaurant_id):
    if request.method == 'GET':
        return render_template('create_menu_item.html', form=CreateMenuItem(), restaurant_id=restaurant_id)


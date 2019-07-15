from flask import render_template, request, flash, redirect, url_for
from .. import db
from .forms import CreateMenuItem
from ..models import MenuItem
from . import menu_items as app_menu_items


@app_menu_items.route('/')
def show_menu(restaurant_id):
    menu_items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menus.html', menu_items=menu_items, restaurant_id=restaurant_id)


@app_menu_items.route('/new', methods=['GET', 'POST'])
def create_menu(restaurant_id):
    if request.method == 'GET':
        return render_template('create_menu_item.html', form=CreateMenuItem(), restaurant_id=restaurant_id)

    if request.method == 'POST':
        form = CreateMenuItem()
        if form.validate_on_submit():
            menu_item = MenuItem()
            menu_item.name = form.name.data
            menu_item.description = form.description.data
            menu_item.course = form.course.data
            menu_item.price = form.price.data
            menu_item.restaurant_id = restaurant_id
            db.session.add(menu_item)
            db.session.commit()
            flash('New Menu item created!')
        else:
            flash('Unspected error on create menu item!')

        return redirect(url_for('.show_menu', restaurant_id=restaurant_id))


from flask import render_template, request, flash, redirect, url_for
from . import restaurants
from .forms import CreateRestaurant
from .. import db
from ..models import Restaurant, MenuItem


@restaurants.route('/')
def show_restaurants():
    restaurants = db.session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@restaurants.route('/<int:restaurant_id>/')
@restaurants.route('/<int:restaurant_id>/menu/')
def show_menu(restaurant_id):
    menu_items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menus.html', menu_items=menu_items)


@restaurants.route('/new', methods=['GET','POST'])
def create_restaurant():
    if request.method == 'GET':
        return render_template('create_restaurant.html', form=CreateRestaurant())
    if request.method == 'POST':
        form = CreateRestaurant()
        if form.validate_on_submit():
            restaurant = Restaurant()
            restaurant.name = form.name.data
            db.session.add(restaurant)
            db.session.commit()
            flash('New restaraunt created!')
            return redirect(url_for('.show_restaurants'))

        return 'aconteceu algo de errado'

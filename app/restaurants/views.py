from flask import render_template, request, flash, redirect, url_for
from . import restaurants as app_restaurants
from .forms import CreateRestaurant, EditRestaurant, DeleteRestaurant
from .. import db
from ..models import Restaurant


@app_restaurants.route('/')
def show_restaurants():
    restaurants = db.session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app_restaurants.route('/new', methods=['GET','POST'])
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


@app_restaurants.route('/<int:restaurant_id>/edit', methods=['GET','POSt'])
def edit_restaurant(restaurant_id):

    if request.method == 'GET':
        restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).first()
        if restaurant is not None:
            form = EditRestaurant()
            form.name.data = restaurant.name
            form.id.data = restaurant.id
            return render_template('edit_restaurant.html', form=form)
        else:
            flash('Pay attention, unspected error on edit restaurant ' + restaurant_id)
            return redirect(url_for('.show_restaurants'))

    if request.method == 'POST':
        form = EditRestaurant()
        restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
        if restaurant is not None and form.validate_on_submit():
            restaurant.name = form.name.data
            db.session.add(restaurant)
            db.session.commit()
            flash('Restaurant edited!')
            return redirect(url_for('.show_restaurants'))


@app_restaurants.route('/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):

    if request.method == 'GET':
        restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).first()
        if restaurant is not None:
            form = DeleteRestaurant()
            return render_template('delete_restaurant.html', form=form, restaurant=restaurant)
        else:
            flash('Pay attention, uspected error on delete restaurant')
            return redirect(url_for('.show_restaurants'))

    if request.method == 'POST':
        restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
        if restaurant is not None:
            db.session.delete(restaurant)
            db.session.commit()
            flash('Restaurant deleted!')
        else:
            flash('Pay attention, uspected error on delete restaurant')

        return redirect(url_for('.show_restaurants'))
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'restaurantmenu.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Restaurant(db.Model):

    __tablename__ = 'restaurant'

    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)


class MenuItem(db.Model):
    
    __tablename__ = 'menu_item'

    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(250))
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    restaurant = db.relationship(Restaurant)


@app.route('/restaurants/')
@app.route('/')
def show_restaurants():
    return render_template('index.html')


@app.route('/restaurants/new/')
def create_restaurant():
    return 'create a new restaurant here'


@app.route('/restaurants/<int:restaurant_id>/edit/')
def edite_restaurant(restaurant_id):
    return 'edit you restaurant here'


@app.route('/restaurants/<int:restaurant_id>/delete/')
def delete_restaurant(restaurant_id):
    return 'delte you restaurant here'


@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def show_menu(restaurant_id):
    return 'this page is the menu for restaurant'


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/')
def show_menu_item(restaurant_id, menu_id):
    return ''


@app.route('/restaurants/<int:restaurant_id>/menu/new/')
def create_menu_item(restaurant_id):
    return 'this page is for making a new menu item for restaurant'


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def edit_menu_item(restaurant_id, menu_id):
    return ''

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def delete_menu_item(restaurant_id, menu_id):
    return ''



from . import db


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
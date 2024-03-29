from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .restaurants import restaurants as restaurants_blueprint
    app.register_blueprint(restaurants_blueprint, url_prefix='/restaurants')

    from .menu_items import menu_items as menu_items_blueprint
    app.register_blueprint(menu_items_blueprint, url_prefix='/<int:restaurant_id>/menu')

    return app

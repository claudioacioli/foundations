from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired


class CreateRestaurant(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    submit = SubmitField('Create!')


class EditRestaurant(FlaskForm):
    id = HiddenField()
    name = StringField('Name:', validators=[DataRequired()])
    submit = SubmitField('Edit!')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CreateMenuItem(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    description = TextAreaField('Description:')
    course = TextAreaField('Course:')
    price = StringField('Price: ', validators=[DataRequired()])
    submit = SubmitField('Create!')


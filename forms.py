from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class bookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    writer = TextAreaField('writer', validators=[DataRequired()])
    date = IntegerField('date', validators=[DataRequired()])

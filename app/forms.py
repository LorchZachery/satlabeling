from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired, NumberRange, Regexp


class NextForm(FlaskForm):
     submit2 = SubmitField('N\u0332ext', id="submit2")

class PrevForm(FlaskForm):
    submit3 = SubmitField('P\u0332revious')
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired, NumberRange, Regexp

class BandForm(FlaskForm):
    band_num = IntegerField('Band Number', validators=(validators.Optional(),))
    rgb = BooleanField('Show RGB?', validators=(validators.Optional(),))
    submit = SubmitField('Submit')
    
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, IntegerField, validators, FileField
from wtforms.validators import DataRequired, NumberRange, Regexp

class BandForm(FlaskForm):
    band_num = IntegerField('Band Number', validators=(validators.Optional(),))
    rgb = BooleanField('Show RGB?', validators=(validators.Optional(),))
    submit = SubmitField('Submit')

class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField('Submit')

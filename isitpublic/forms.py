from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IpForm(FlaskForm):
    address = StringField('IP Address', validators=[DataRequired()])
    submit = SubmitField('is it public?')

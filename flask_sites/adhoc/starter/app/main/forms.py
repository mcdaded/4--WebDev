"""
danmcdade_flask - 'main/forms' created on 2/1/2018 at 5:17 PM

@author: dmcdade
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


# Forms
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


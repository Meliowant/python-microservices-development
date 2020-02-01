from flask_wtf import FlaskForm
import wtforms as f
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    email = f.StringField(validators=[DataRequired()])
    firstname = f.StringField('firstname')
    lastname = f.StringField('lastname')
    pass

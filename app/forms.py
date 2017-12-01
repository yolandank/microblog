from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
class LoginForm(Form):
    openid = StringField('你的openid', validators=[DataRequired()])
    remember_me = BooleanField('是否记住', default=False)
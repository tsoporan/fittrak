from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

from .models import User

class EmailRegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        user = User.query.filter(email=self.email.data).first()

        # Find user
        if not user:
            self.email.errors.append('User or password is incorrect.')
            return False

        # Check password
        if not user.check_password(self.password.data):
            self.password.errors.append('User or password is incorrect.')
            return False

        return True

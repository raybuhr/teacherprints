from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from tp_app.models import User
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Sign in'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different username'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different email address'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l('Please use a different username'))


class EmptyForm(FlaskForm):
    submit = SubmitField(_l('Submit'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validator=[DataRequired(), Email()])
    submit = SubmitField(_l('Request password reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request password reset'))




# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins

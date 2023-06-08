
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class MyForm(FlaskForm):
    name = StringField(label = "Username", validators= [DataRequired(message="Username is required")])
    email_address =  StringField(label = "Email_address", validators= [ DataRequired("Email field is required"), Email()])
    password = PasswordField(label= "Password", validators= [ DataRequired(message= "Password field is required"), Length(min = 8)])
    password2 = PasswordField(label = "Confirm Password",  validators= [DataRequired(), EqualTo("password", message= "The inputed password does not match")])
    submit = SubmitField(label = "Create Account")

    
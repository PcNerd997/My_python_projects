from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    name = StringField(label = "Name,", validators= [validators.DataRequired(message= "name is required")])
    email = StringField(label = "Email", validators= [validators.Email( message= "invalid email"), validators.DataRequired(message= "email is required")])
    password = PasswordField(label = "Password", validators= [validators.DataRequired(message= "password is required"), validators.length(min = 8, message = "password must be more than 8 characters")])
    submit = SubmitField(label = "Login")



app = Flask(__name__)
app.secret_key = "I_Want_This_Key_To_Be_Secrete"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/successful", methods = ['POST'])
def succesful():
    return "<h1>You've successfully logged in</h1>"

@app.route("/login", methods = ['POST', 'GET'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = form)



if __name__ == '__main__':
    app.run(debug=True)
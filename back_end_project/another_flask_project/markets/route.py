from markets import app
from flask import render_template, redirect, url_for
from markets.models import Item, User
from markets.forms import MyForm
from markets import db

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)


@app.route("/login", methods = ['POST', 'GET'])
def login():
    forms = MyForm()
    if forms.validate_on_submit():
        new_user = User(username = forms.name.data, email_address = forms.email_address.data, password_hash = forms.password.data)
        if not User.query.filter_by(username = forms.name.data).first() and not User.query.filter_by(email_address = forms.email_address.data).first():
            db.session.add(new_user)
            db.session.commit()
            print(forms.password.data)
            return redirect( url_for("market"))
    return render_template("login.html", forms = forms)

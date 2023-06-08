from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = '2ad4dbd22d1035fefcbf8dff'
app.app_context().push()
db = SQLAlchemy(app)

from markets import route
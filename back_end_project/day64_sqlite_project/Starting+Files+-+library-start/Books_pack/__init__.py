from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.app_context().push()
db = SQLAlchemy(app)


import Books_pack.route

# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.app_context().push()
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(60), nullable = False, unique = True)
    author = db.Column(db.String(60), nullable = False)
    rating = db.Column(db.Float(), nullable = False)

    def __repr(self):
        return f"User {self.title}"
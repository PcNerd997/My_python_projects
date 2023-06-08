from Books_pack import app, db
from Books_pack.models import Books
from flask import render_template, request, redirect, url_for
@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', book_list = all_books)


@app.route("/add", methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        rating = request.form['rating']
        new_book = Books(title = book_name, author = book_author, rating = rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<book_>", methods = ['POST', 'GET'])
def edit_rating(book_):
    book = Books.query.get(book_)
    if request.method == 'POST':
        book.rating = request.form['change_rating']
        db.session.commit()
        return redirect(url_for('home'))
   
    return render_template('edit.html', book = book)

@app.route("/detele/<book_id>")
def delete(book_id):
    book = Books.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))
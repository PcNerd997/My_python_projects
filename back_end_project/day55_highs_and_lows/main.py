from flask import Flask
import random

app = Flask(__name__)
number_generated = random.randint(0, 9)


@app.route("/")
def say_somthing():
    return "<h1 style = 'color: red'>Guess a number from 0 to 9</h1>" \
           "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt = 'number from 1 to 9'>"


@app.route("/<int:guessed_number>")
def check_number(guessed_number):
    if guessed_number > number_generated:
        return "<h1 style = 'color: yellow'>Too High, Try Again</h1>" \
               "<img src = 'https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif'>"
    elif guessed_number < number_generated:
        return '<h1 style = "color: purple">Too Low, Try Again</h1>' \
               '<img src = "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif">'
    else:
        return "<h1 style = 'color: green'>You Found Me!</h1>" \
               "<img src = 'https://media.giphy.com/media/E0cyxhawhe9dm/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug = True)
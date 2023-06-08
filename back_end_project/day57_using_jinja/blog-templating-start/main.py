from flask import Flask, render_template
import requests


app = Flask(__name__)

respons = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391")
blogs = respons.json()
@app.route('/blog')
def home():

    return render_template("index.html", blogs = blogs)


@app.route('/blog/<int:id>')
def post(id):
    print(blogs[int(id)]['title'])
    return render_template("post.html", id_to_display = id - 1, blogs_ = blogs)

if __name__ == "__main__":
    app.run(debug=True)
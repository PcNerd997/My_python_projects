import requests
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def say_hello():
    respons = requests.get(url = " https://api.npoint.io/c790b4d5cab58020d391")
    fake_blog = respons.json()
    return render_template("test_html.html", blogs = fake_blog)


if __name__ == "__main__":
    app.run(debug= True)
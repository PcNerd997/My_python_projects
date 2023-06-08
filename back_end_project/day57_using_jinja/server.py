from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

genderize_api_key = "skHT2wdlquSYQCWjHe6hj78KZXTL7yZgTv4u"
genderize_url = "https://gender-api.com/get"
agify_url = "https://api.agify.io"
app = Flask(__name__)

@app.route("/<name>")
def say_hello(name):
    
    genderize_respons = requests.get(url = genderize_url, params= {"name": name, "key": genderize_api_key})
    gender = genderize_respons.text.strip('{ }').strip(":").split('"')[15]
    respons = requests.get( url = agify_url, params= {"name": name})
    return_text = respons.text
    age = int((return_text.strip('{ }').strip(':').split('"')[2].strip(":,")))
    return render_template("index.html", gen = gender, ag = age, user_name = name)

if __name__ == "__main__":
    app.run(debug= True)
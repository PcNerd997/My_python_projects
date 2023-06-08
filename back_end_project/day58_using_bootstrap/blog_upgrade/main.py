from flask import Flask, render_template, request
import requests
from datetime import datetime
from smtplib import SMTP



date = datetime.now()
formated_date = date.strftime("%B %d, %Y")
app = Flask(__name__)   

respons = requests.get(url = "https://api.npoint.io/a22f803a5b40fb3d1450")
data = respons.json()

@app.route("/")
def render_html():
    return render_template("index.html", blogs = data, date = formated_date)

@app.route("/about")
def about_page():
    return render_template("about.html")


def receive_form():
    connection = SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = "ajayihabeeb977@gmail.com", password= "pstxprzhhlrjjlqd")
    
    username = request.form['username']
    email_address = request.form['email_address']
    phone_number = request.form['phone number']
    message = request.form['message']

    formatted_message = f"name: {username}\nemail_address: {email_address}\nphone_number: {phone_number}\n\nmessage: {message}"
    connection.sendmail(from_addr='ajayihabeeb977@gmail.com', to_addrs='ajayihabeeb997@gmail.com', msg= formatted_message) 
    




@app.route("/contact", methods = ['POST', 'GET'])
def contact_page():
    if request.method == 'POST':
        receive_form()
        return render_template('contact.html', information = 'Successfully Sent Your Messages')
    else:
        return render_template('contact.html', information = "Contact Me")

@app.route('/post/<blog_id>')
def post_render(blog_id):
    print(data[1]['image_url'])
    return render_template('post.html', blog_index = int(blog_id), blogs = data, date = formated_date)

# @app.route('/form-entry', methods = ['POST'])



if __name__ == "__main__":
    app.run(debug=True)
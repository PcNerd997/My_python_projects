from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import pandas, csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField( label = 'Cafe name', validators=[DataRequired()])
    location = StringField( label = "Cafe location on Google Map (URL)", validators=[DataRequired(), URL()])
    open_time = StringField(label="Open time e.g 8:00AM",  validators= [DataRequired()])
    close_time = StringField(label="Close time e.g 6:00PM", validators= [DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", choices= ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️","☕️☕️☕️☕️☕️"])
    wifi_rating = SelectField(label="Wifi Strenght Rating", choices= ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"] )
    power_stability = SelectField(label="Power Stability Rating", choices= ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌" ])
    submit = SubmitField(label='Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
        new_entry = [{"Cafe Name": form.cafe.data, 
                      "Location": form.location.data, 
                      "Open": form.open_time.data, 
                      "Close": form.close_time.data,
                       "Coffee": form.coffee_rating.data,
                      "Wifi": form.wifi_rating.data,
                      "Power": form.power_stability.data}] 

        new_entry_dataframe = pandas.DataFrame(new_entry)
        new_entry_dataframe.to_csv("Starting+Files+-+coffee-and-wifi/cafe-data.csv", mode = "a", header= False, index=False) 
        return cafes()     
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Starting+Files+-+coffee-and-wifi/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        print(csv_data)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

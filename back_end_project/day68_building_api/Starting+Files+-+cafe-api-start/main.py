from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"CAfe {self.name}"




@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods = ['GET'])
def random():
    random_cafe = choice(Cafe.query.all())
    return jsonify(cafe = random_cafe.to_dict())


@app.route("/all", methods = ['GET'])
def all():
    cafes = Cafe.query.all()
    all_cafe = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes = all_cafe)

@app.route("/search", methods = ['GET'])
def search():
    request_query = request.args.get('loc')
    print(request_query)
    search_respons = Cafe.query.filter_by(location = request_query).first()
    if search_respons:
        return jsonify(cafes = search_respons.to_dict())
        print("you are right")
    else:
        return jsonify(error = {"Not Found": "Sorry, we dont have a location at that point"})


@app.route("/add", methods = ['POST', 'GET'])
def add():
    new_cafe = Cafe(name = request.form.get('name'),
                    map_url = request.form.get('map_url'),
                    img_url = request.form.get('img_url'),
                    location = request.form.get('location'),
                    seats = request.form.get('seat'),
                    has_toilet = request.form.get('has_toilet'),
                    has_wifi = request.form.get('has_wifi'),
                    has_sockets = request.form.get('has_sockets'),
                    can_take_calls = request.form.get('can_take_calls'),
                    coffee_price = request.form.get('coffee_price'),
                    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
    except:
        return jsonify(respons = { "Failed": "The new entry was not successfully add"
        })
    else:

        return jsonify(respons = {'success': "Successfully add the new cafe"})
   
    

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)



#to get a parameter from the url, which will appear a question mark for instance url/name?loc=username 
# request.arg.get('loc')
from markets import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    email_address = db.Column(db.String(length = 60), nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 60), nullable = False)
    items = db.relationship('Item', backref = "owned_user", lazy = True)

    def __repr__(self):
        return f"User {self.username}"

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable= False)
    discription = db.Column(db.String(length = 1024), nullable = False, unique = True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item {self.name}"
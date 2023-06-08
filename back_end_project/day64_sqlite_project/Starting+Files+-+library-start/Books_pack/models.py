from Books_pack import db
class Books(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(60), nullable = False, unique = True)
    author = db.Column(db.String(60), nullable = False)
    rating = db.Column(db.Float(), nullable = False)

    def __repr(self):
        return f"User {self.title}"
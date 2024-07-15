from app.extensions import db

class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rating = db.Column(db.Integer)
  text = db.Column(db.String(256))
  author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  author = db.Column(db.String(80))
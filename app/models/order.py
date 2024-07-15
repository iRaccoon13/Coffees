from app.extensions import db
import datetime

class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  coffee = db.Column(db.Text, nullable=False)
  flavor = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, default=datetime.datetime.now)
  is_archived = db.Column(db.Boolean, default=False)
  favorite = db.Column(db.Boolean, default=False)
  name = db.Column(db.Text, nullable=False)
  special = db.Column(db.Text)
  author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  is_completed = db.Column(db.Boolean, default=False)
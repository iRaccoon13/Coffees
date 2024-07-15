from app.extensions import db

class Menu(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	itemtype = db.Column(db.Text, nullable=False)
	name = db.Column(db.Text, nullable=False)
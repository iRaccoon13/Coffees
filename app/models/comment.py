from app.extensions import db

class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(100))
  date = db.Column(db.DateTime, default=datetime.datetime.now)
  #post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
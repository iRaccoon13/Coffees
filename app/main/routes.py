from app.main import bp
from flask import render_template
from app.extensions import db
from flask_login import current_user

@bp.route('/')
def index():
  return render_template("index.html", faves=[order for order in current_user.orders if order.favorite] if current_user.is_authenticated else [])
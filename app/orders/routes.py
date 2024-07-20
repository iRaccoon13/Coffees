from datetime import datetime
from dateutil import parser as dateutil_parser
from app.extensions import db
from flask import render_template, request, abort, redirect, url_for
from app.orders import bp
from flask_login import login_required, current_user
from app.models.order import Order
from app.models.user import User
from app.models.menu import Menu
import json

@bp.route("/order/<id>/", methods=["GET", "PATCH"])
def order_by_id(id):
  order = Order.query.get_or_404(id)
  if request.method == "GET":
    return {
      "id": order.id, 
      "coffee": order.coffee, 
      "flavor": order.flavor, 
      "date": order.date,
      "is_archived": order.is_archived,
      "author_id": order.is_archived
    }
  elif request.method == "PATCH":
    order.is_completed = request.json["is_completed"]
    order.is_archived = request.json["is_archived"]
    db.session.commit()
    return "200 OK"

@bp.route("/order/", methods=["POST", "GET"])
def order():
  if request.method == "GET":
    coffees = Menu.query.filter_by(itemtype="coffee").all()
    flavors = Menu.query.filter_by(itemtype="flavor").all()
    return render_template("order.html", coffees=coffees, flavors=flavors)
  if request.method == "POST":
    coffee = request.form.get('coffee')
    flavor = request.form.get('flavor')
    favorite = request.form.get('favorite') if current_user.is_authenticated else False
    caffeine = ("Decaf","Single", "Double", "Triple", "Quadruple")[int(request.form.get("caffeine"))]
    special = request.form.getlist('special')
    special.append(caffeine)
    special = json.dumps(special)
    name = request.form.get('name')
    date = request.form.get('date')
    date = dateutil_parser.parse(date)
    order = Order(coffee=coffee, flavor=flavor, favorite=True if favorite else False, name=name, special=special, date=date)
    if current_user.is_authenticated:
      user = User.query.get(current_user.id)
      user.orders.append(order)
    db.session.add(order)
    db.session.commit()
    return redirect(url_for("orders.success", id=order.id))

@bp.route("/order/<id>/removefavorite/", methods=["POST"])
def removefavorite(id):
  order = Order.query.get_or_404(id)
  order.favorite = False
  db.session.commit()
  return "200 OK"

@bp.route("/order/<id>/copy/", methods=["POST"])
def copyorder(id):
  order = Order.query.get_or_404(id)
  neworder = Order(
    coffee=order.coffee,
    flavor=order.flavor,
    special=order.special,
    name=order.name)
  current_user.orders.append(neworder)
  db.session.add(neworder)
  db.session.commit()
  return "200 OK"


@bp.route("/orders/")
@login_required
def orders():
  if current_user.id != 1:
    abort(401)
  orders = [order for order in Order.query.filter_by(is_archived=False).all() if order.date < datetime.now()]
  orders.sort(key=lambda i: i.date)
  return render_template("orders.html", orders=orders)

@bp.route("/order/<id>/success/")
def success(id):
  order = Order.query.get_or_404(id)
  date = order.date
  place = len([i.id for i in Order.query.filter_by(is_archived=False) if i.date <= date])
  return render_template("ordersuccess.html", place=place, id=id, order=order)

import datetime
from app.extensions import db
from flask import render_template, request, abort, redirect, url_for
from app.menu import bp
from flask_login import login_required, current_user
from app.models.user import User
from app.models.menu import Menu

@bp.route("/menu/", methods=["GET", "PUT"])
@login_required
def menu():
  if current_user.id != 1:
    abort(403)
  elif request.method == "GET":
    coffees = Menu.query.filter_by(itemtype="coffee").all()
    flavors = Menu.query.filter_by(itemtype="flavor").all()
    return render_template("menuupdate.html", coffees=coffees, flavors=flavors)
  elif request.method == "PUT":
    Menu.query.delete()
    for i in request.json["coffees"]:
      db.session.add(Menu(itemtype="coffee", name=i))
    for i in request.json["flavors"]:
      db.session.add(Menu(itemtype="flavor", name=i))
    db.session.commit()
    return "200 OK"
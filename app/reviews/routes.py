import datetime
from app.extensions import db
from flask import render_template, request, abort, redirect, url_for
from app.reviews import bp
from flask_login import login_required, current_user
from app.models.user import User
from app.models.review import Review

@bp.route("/reviews/", methods=["GET", "POST"])
def reviews():
  if request.method == "GET":
    reviews = Review.query.all()
    return render_template("reviews.html", reviews=reviews)
  elif request.method == "POST":
    if not current_user.is_authenticated:
      abort(403)
    else: 
      rating = request.form["rating"]
      body = request.form["body"]
      newreview = Review(text=body, rating=rating, author=current_user.username)
      current_user.reviews.append(newreview)
      db.session.add(newreview)
      db.session.commit()
      return redirect(url_for("reviews.reviews"))
      

@bp.route("/reviews/<int:id>/delete", methods=["GET"])
@login_required
def delreview(id):
  review = Review.query.get_or_404(id)
  if current_user.id != review.author_id:
    abort(403)
  else:
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("reviews.reviews"))


@bp.route("/newreview/", methods=["GET"])
@login_required
def leave_a_review():
  if request.method == "GET":
    return render_template("leave_a_review.html")
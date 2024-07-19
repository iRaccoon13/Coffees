from app.auth import bp
from flask import render_template, request, redirect, url_for, flash
from app.extensions import login_manager, db
from app.models.user import User
import bcrypt
from flask_login import login_required, login_user, logout_user



@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@bp.route("/signup", methods=["GET", "POST"])
def signup():
  try:
    if request.method == "GET":
      return render_template("signup.html")
  except RuntimeError:
    request_exists = False
  else: 
    request_exists = True
  password = request.form.get('password')
  username = request.form.get('username')

  user = User.query.filter_by(username=username).first() 
  if user: 
    flash("User with that username already exists", category="info")
    return redirect(url_for('auth.signup'))
    
  new_user = User(username=username, password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))

  # add the new user to the database
  db.session.add(new_user)
  db.session.commit()
  if request_exists:
    login_user(new_user)
    return redirect(url_for('main.index'))
  else:
    return new_user

@bp.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  username = request.form.get('username')
  password = request.form.get('password')
  user = User.query.filter_by(username=username).first()
  if user:
    if bcrypt.checkpw(password.encode('utf-8'), user.password):
      login_user(user)
      return redirect(url_for('main.index'))
    else:
      flash('Check password and username')
      return redirect(url_for('auth.login'))
  else:
    flash('No account with that username exists')
    return redirect(url_for('auth.signup'))

@bp.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))




  
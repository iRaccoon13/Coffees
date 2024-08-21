from flask import Flask
from config import Config

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  # Initialize Flask extensions here
  from app.extensions import db, login_manager, migrate, sock
  
  db.init_app(app)
  
  migrate.init_app(app, db)
  
  login_manager.init_app(app)
  login_manager.login_view = "auth.login"

  sock.init_app(app)
  
  # Register blueprints here
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)
  
  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp)
  
  from app.orders import bp as orders_bp
  app.register_blueprint(orders_bp)

  from app.menu import bp as menu_bp
  app.register_blueprint(menu_bp)

  from app.reviews import bp as reviews_bp
  app.register_blueprint(reviews_bp)

  return app
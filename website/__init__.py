from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    db.init_app(app)

    from .features import feature
    app.register_blueprint(feature)

    from .models import Overview
    with app.app_context():
        db.create_all()

    return app
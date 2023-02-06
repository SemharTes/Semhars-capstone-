from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)
    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.symptom import Symptom
    from app.models.admin import Admin

    # Register Blueprints
    from .symptom_routes import symptoms_bp
    app.register_blueprint(symptoms_bp)
    from .admin_routes import admin_bp
    app.register_blueprint(admin_bp)

    CORS(app)

    return app
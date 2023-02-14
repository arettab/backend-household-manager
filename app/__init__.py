from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/household_manager_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import event
    from .routes import household
    from .routes import users
    from .routes import invitation


    app.register_blueprint(event.bp)
    app.register_blueprint(household.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(invitation.bp)

    from app.models.household import Household
    from app.models.user import User
    from app.models.invitation import Invitation

    return app
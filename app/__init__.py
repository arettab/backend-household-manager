from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/household_manager_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import event
    from .routes import household
    from .routes import user

    app.register_blueprint(event.bp)
    app.register_blueprint(household.bp)
    app.register_blueprint(user.bp)

    from app.models.event import Event
    from app.models.household import Household
    from app.models.user import User

    return app
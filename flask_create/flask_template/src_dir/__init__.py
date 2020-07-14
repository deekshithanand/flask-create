from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # load app configs
    app.config.from_object('config.Config')

    # initialize sqlalchemy
    db.init_app(app)

    with app.app_context():
        # import and register blueprint here.
        pass

    return app

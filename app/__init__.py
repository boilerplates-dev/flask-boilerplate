from flask import Flask

from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.redis import Redis
from rq import Queue

from config import config

mail = Mail()
db = SQLAlchemy()
redis = Redis()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    redis.init_app(app)
    app.q = Queue(connection=redis.connection)

    from home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app

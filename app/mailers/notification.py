import os
from flask.ext.rq import job
from app import create_app, redis

app = create_app(os.getenv('FLASK_ENV') or 'default')


@job('low')
def send_welcome_email(key):
    with app.app_context():
        redis.incr(key)
        print "Welcome!!!"

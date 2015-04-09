from flask import current_app, render_template

from . import home


@home.route('/')
def index():
    current_app.q.enqueue("app.mailers.notification.send_welcome_email",
                          "Welcome to flasky!!!")
    return render_template('home/index.html')

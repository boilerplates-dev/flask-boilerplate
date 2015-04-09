import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/development.sqlite')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'


class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/test.sqlite')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'


class Production(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/production.sqlite')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'

config = {
    'development': Development,
    'test': Test,
    'production': Production,
    'default': Development
}

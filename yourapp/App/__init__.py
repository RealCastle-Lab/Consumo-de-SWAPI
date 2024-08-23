# app/__init__.py
from flask import Flask
from flask_mail import Mail
from .celery import make_celery

def create_app():
    app = Flask(__name__)
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your-email@example.com'
    app.config['MAIL_PASSWORD'] = 'your-password'
    
    mail = Mail(app)
    celery = make_celery(app)

    from .routes import configure_routes
    configure_routes(app, mail, celery)

    return app

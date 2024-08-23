# app/routes.py
from flask import render_template, request, jsonify
from flask_mail import Message

def configure_routes(app, mail, celery):

    @app.route('/send_mail', methods=['POST'])
    def send_mail():
        email = request.form['email']
        send_async_email.delay(email)
        return jsonify({'message': 'Email sent!'})

    @celery.task
    def send_async_email(email):
        msg = Message("Hello from Flask",
                      sender="your-email@example.com",
                      recipients=[email])
        msg.body = "This is a test email sent from a background Celery task."
        mail.send(msg)

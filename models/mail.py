from flask_mail import Message
from app import mail
from flask import render_template
from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, **kwargs):
    from app import app

    app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[FLASKY]'
    app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = kwargs.get('body', '')
    msg.html = kwargs.get('html', '')

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
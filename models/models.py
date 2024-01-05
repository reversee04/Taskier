# models/models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_login import UserMixin
db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(250))

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(1000000), nullable=False)
    attachment = db.Column(db.String(100), nullable=False)


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_migrate import Migrate
from models.models import db, User
from flask_mail import Mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'routes.login' 

db.init_app(app)

migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

from routes.routes import routes_blueprint
app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)

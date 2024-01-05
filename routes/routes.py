# routes/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import db, User, Task
from flask import session
from flask_login import current_user, login_user, logout_user, login_required

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def homepage():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@routes_blueprint.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already exists. Please use a different email.', 'error')
            return redirect(url_for('routes.signup'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('routes.login'))

    return render_template('signup.html')

@routes_blueprint.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user )
            flash('login succesful', 'success')

            return redirect(url_for('routes.homepage'))
        else:
            flash('Invalid email or password. Pleas try again', 'error')

    return render_template('login.html', current_user=current_user)

@routes_blueprint.route('/tasks.html')
def taskspage():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@routes_blueprint.route('/addtasks.html')
def addtask():
    return render_template('addtasks.html')

@routes_blueprint.route('/emails.html', methods=['GET', 'POST'])
def emailTask():
    from models.mail import send_mail
    if request.method == 'POST':
        to_email = request.form['to_email']
        subject = request.form['email_subject']
        email_body = request.form['email_body']

        sender_email = current_user.email

        send_mail(to_email, subject, email_body=email_body)

        flash('Email sent successfully', 'success')
        return redirect(url_for('routes.emailTask'))

    return render_template('emails.html')

from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user

from . import app, db
from .forms import EmailRegistrationForm, LoginForm
from .models import User

import datetime

@app.route('/')
def index():
    return render_template('index.html', user=current_user)

@app.route('/register/complete/')
def register_complete():
    return render_template('registration_complete.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register a user"""

    form = EmailRegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            user.email = form.email.data
            user.set_password(form.password.data)

            # Add user to DB
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('register_complete'))

    return render_template('registration.html', form=form)

@app.route('/login/', methods=['GET','POST'])
def login():
    """Log a user in"""

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # Log the user in
            user = User.query.filter_by(email=form.email.data).first()
            login_user(user)

            return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/logout/')
def logout():
   logout_user()
   return redirect(url_for('index'))

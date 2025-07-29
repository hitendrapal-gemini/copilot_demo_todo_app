from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from user import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.validate(username, password)
        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('tasks.home'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

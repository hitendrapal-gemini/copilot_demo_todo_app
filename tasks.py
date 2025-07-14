from flask import Blueprint, request, redirect, url_for, render_template, flash
from utils import generate_task_id  # Assuming this function is defined in utils.py
from config import Config
from datetime import datetime
from flask_login import login_user, logout_user, login_required, current_user
from user import User, users

tasks = Blueprint('tasks', __name__)

TASK_DICT = {'Items': []}
ALL_TAGS = set()  # Store all tags for auto-suggestion



@tasks.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('tasks.home'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@tasks.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'info')
    return redirect(url_for('tasks.login'))

@tasks.route('/')
@login_required
def home():
    global TASK_DICT, ALL_TAGS
    tasks_data = TASK_DICT.get('Items', [])
    search_query = request.args.get('search', '').strip()
    if search_query:
        tasks_data = [
            task for task in tasks_data
            if search_query.lower() in task['task_name'].lower()
        ]
    # Collect all tags for auto-suggestion
    ALL_TAGS = set(tag for task in TASK_DICT['Items'] for tag in task.get('tags', []))
    return render_template('dashboard.html', tasks=tasks_data, search=search_query, user=current_user, all_tags=list(ALL_TAGS))


@tasks.route('/add', methods=['POST'])
def add_task():
    global TASK_DICT, ALL_TAGS
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')
    tags = request.form.getlist('tags')  # Get tags as list

    # Validate due date: must be today or in the future
    if due_date:
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
            today = datetime.today().date()
            if due_date_obj < today:
                flash('Due date cannot be in the past. Please select today or a future date.', 'error')
                return redirect(url_for('tasks.home'))
        except ValueError:
            flash('Invalid due date format.', 'error')
            return redirect(url_for('tasks.home'))

    if task_name:
        task_id = generate_task_id(TASK_DICT)
        TASK_DICT['Items'].append({
            'task_id': task_id,
            'task_name': task_name,
            'due_date': due_date,
            'completed': False,
            'tags': tags,
        })
        ALL_TAGS.update(tags)
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.home'))

@tasks.route('/complete/<task_id>', methods=['POST'])
def complete_task(task_id):

    # update the task in TASK_DICT to mark it as completed
    global TASK_DICT
    
    task_data = {}
    for task in TASK_DICT['Items']:
        if task['task_id'] == task_id:
            task['completed'] = True
            task_data = task
            break
    
    if task_data:
        task_description = task_data['task_name']
        flash(f'Task {task_description} marked as completed and email notification sent', 'success')
    else:
        flash('Task not found', 'danger')

    return redirect(url_for('tasks.home'))

@tasks.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):

    global TASK_DICT
    # Remove the task from TASK_DICT
    TASK_DICT['Items'] = [task for task in TASK_DICT['Items'] if task['task_id'] != task_id]
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.home'))

@tasks.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    global TASK_DICT, ALL_TAGS
    task_to_edit = None
    for task in TASK_DICT['Items']:
        if task['task_id'] == task_id:
            task_to_edit = task
            break

    if not task_to_edit:
        flash('Task not found.', 'error')
        return redirect(url_for('tasks.home'))

    if request.method == 'POST':
        new_name = request.form.get('task_name')
        new_due_date = request.form.get('due_date')
        new_tags = request.form.getlist('tags')

        # Validate due date: must be today or in the future
        if new_due_date:
            try:
                due_date_obj = datetime.strptime(new_due_date, "%Y-%m-%d").date()
                today = datetime.today().date()
                if due_date_obj < today:
                    flash('Due date cannot be in the past. Please select today or a future date.', 'error')
                    return redirect(url_for('tasks.edit_task', task_id=task_id))
            except ValueError:
                flash('Invalid due date format.', 'error')
                return redirect(url_for('tasks.edit_task', task_id=task_id))

        if new_name:
            task_to_edit['task_name'] = new_name
        task_to_edit['due_date'] = new_due_date
        task_to_edit['tags'] = new_tags
        ALL_TAGS.update(new_tags)
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.home'))

    # GET request: render edit form
    ALL_TAGS = set(tag for task in TASK_DICT['Items'] for tag in task.get('tags', []))
    return render_template('edit_task.html', task=task_to_edit, all_tags=list(ALL_TAGS))
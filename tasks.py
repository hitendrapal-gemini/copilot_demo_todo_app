from flask import Blueprint, request, redirect, url_for, render_template, flash
from utils import generate_task_id  # Assuming this function is defined in utils.py
from config import Config
from datetime import datetime
from flask_login import login_required, current_user

tasks = Blueprint('tasks', __name__)

TASK_DICT = {'Items': []}  # Placeholder for task list, not used in this version



@tasks.route('/')
@login_required
def home():
    # Fetch tasks from DynamoDB
    global TASK_DICT
    tasks_data = TASK_DICT.get('Items', [])
    search_query = request.args.get('q', '').strip()
    if search_query:
        tasks_data = [
            task for task in tasks_data
            if search_query.lower() in task.get('task_name', '').lower()
        ]
    return render_template('dashboard.html', tasks=tasks_data, current_user=current_user)


@tasks.route('/add', methods=['POST'])
@login_required
def add_task():
    global TASK_DICT
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')  # Get due date from form

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
            'due_date': due_date,  # Store due date
            'completed': False,
        })
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.home'))

@tasks.route('/complete/<task_id>', methods=['POST'])
@login_required
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
@login_required
def delete_task(task_id):

    global TASK_DICT
    # Remove the task from TASK_DICT
    TASK_DICT['Items'] = [task for task in TASK_DICT['Items'] if task['task_id'] != task_id]
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.home'))

@tasks.route('/edit/<task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    global TASK_DICT
    # Find the task to edit
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
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.home'))

    # GET request: render edit form
    return render_template('edit_task.html', task=task_to_edit, current_user=current_user)
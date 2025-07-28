from flask import Blueprint, request, redirect, url_for, render_template, flash
from utils import generate_task_id  # Assuming this function is defined in utils.py
from config import Config

tasks = Blueprint('tasks', __name__)

TASK_DICT = {'Items': []}  # Placeholder for task list, not used in this version


@tasks.route('/')
def home():
    # Fetch tasks from DynamoDB
    global TASK_DICT
    tasks_data = TASK_DICT.get('Items', [])
    return render_template('dashboard.html', tasks=tasks_data, edit_task=None)

@tasks.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')
    if task_name:
        task_id = generate_task_id()
        global TASK_DICT
        TASK_DICT['Items'].append({
            'task_id': task_id,
            'task_name': task_name,
            'due_date': due_date,
            'completed': False,
        })
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
    global TASK_DICT
    task = next((t for t in TASK_DICT['Items'] if t['task_id'] == task_id), None)
    if not task:
        flash('Task not found', 'danger')
        return redirect(url_for('tasks.home'))
    if request.method == 'POST':
        new_name = request.form.get('task_name')
        new_due = request.form.get('due_date')
        if new_name and new_due:
            task['task_name'] = new_name
            task['due_date'] = new_due
            flash('Task updated successfully!', 'success')
            return redirect(url_for('tasks.home'))
        else:
            flash('Both name and due date are required.', 'danger')
    # GET: show dashboard with edit form for this task
    tasks_data = TASK_DICT.get('Items', [])
    return render_template('dashboard.html', tasks=tasks_data, edit_task=task)
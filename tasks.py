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
    return render_template('dashboard.html', tasks=tasks_data)

@tasks.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        task_id = generate_task_id()
        global TASK_DICT
        TASK_DICT['Items'].append({
            'task_id': task_id,
            'task_name': task_name,
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
from flask import Blueprint, request, redirect, url_for, render_template, flash

from utils import generate_task_id  # Assuming this function is defined in utils.py

from services import TaskService

tasks = Blueprint('tasks', __name__)


# Global TaskService instance
TASK_DICT = {'Items': []}
task_service = TaskService(TASK_DICT)


@tasks.route('/')
def home():
    tasks_data = task_service.get_tasks()
    return render_template('dashboard.html', tasks=tasks_data)

  
@tasks.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        task_id = generate_task_id()
        task_service.add_task(task_id, task_name)
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.home'))

  
@tasks.route('/complete/<task_id>', methods=['POST'])
def complete_task(task_id):
    task_data = task_service.complete_task(task_id)
    if task_data:
        task_description = task_data['task_name']
        flash(f'Task {task_description} marked as completed and email notification sent', 'success')
    else:
        flash('Task not found', 'danger')
    return redirect(url_for('tasks.home'))

  
@tasks.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    task_service.delete_task(task_id)
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.home'))

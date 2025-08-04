import json
import os
from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from utils import generate_task_id  # Assuming this function is defined in utils.py
from utils import send_email_notification  # Assumed to be implemented for email sending
from config import Config

DB_PATH = os.path.join(os.path.dirname(__file__), 'db.json')

class TaskDb:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump({'Items': []}, f)

    def _read(self):
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def _write(self, data):
        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=2)

    def list(self):
        data = self._read()
        return data.get('Items', [])

    def save(self, task):
        data = self._read()
        data.setdefault('Items', []).append(task)
        self._write(data)

    def update(self, task_id, updates):
        data = self._read()
        updated = False
        for task in data.get('Items', []):
            if task['task_id'] == task_id:
                task.update(updates)
                updated = True
                break
        self._write(data)
        return updated

    def delete(self, task_id):
        data = self._read()
        items = data.get('Items', [])
        new_items = [task for task in items if task['task_id'] != task_id]
        data['Items'] = new_items
        self._write(data)

    def get(self, task_id):
        data = self._read()
        for task in data.get('Items', []):
            if task['task_id'] == task_id:
                return task
        return None

tasks = Blueprint('tasks', __name__)
task_db = TaskDb()

@tasks.route('/')
@login_required
def home():
    tasks_data = task_db.list()
    search_query = request.args.get('q', '').strip().lower()
    if search_query:
        tasks_data = [
            t for t in tasks_data
            if search_query in t.get('task_name', '').lower()
        ]
    return render_template('dashboard.html', tasks=tasks_data, current_user=current_user)

@tasks.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')
    if task_name:
        # Pass the current task dictionary to generate_task_id
        current_tasks = {"Items": task_db.list()}
        task_id = generate_task_id(current_tasks)
        task = {
            'task_id': task_id,
            'task_name': task_name,
            'completed': False,
            'due_date': due_date,
        }
        task_db.save(task)
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.home'))

@tasks.route('/complete/<task_id>', methods=['POST'])
def complete_task(task_id):
    updated = task_db.update(task_id, {'completed': True})
    task_data = task_db.get(task_id)
    if updated and task_data:
        task_description = task_data['task_name']
        # Send email notification
        try:
            to_email = getattr(Config, 'ADMIN_EMAIL', None)
            if to_email:
                subject = f"Task Completed: {task_description}"
                body = f"The task '{task_description}' has been marked as completed."
                send_email_notification(to_email, subject, body)
                flash(f'Task {task_description} marked as completed and email notification sent', 'success')
            else:
                flash(f'Task {task_description} marked as completed, but ADMIN_EMAIL not configured', 'warning')
        except Exception as e:
            flash(f'Task {task_description} marked as completed, but failed to send email: {e}', 'warning')
    else:
        flash('Task not found', 'danger')
    return redirect(url_for('tasks.home'))

@tasks.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    task_db.delete(task_id)
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.home'))

@tasks.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = task_db.get(task_id)
    if not task:
        flash('Task not found', 'danger')
        return redirect(url_for('tasks.home'))
    if request.method == 'POST':
        new_name = request.form.get('task_name')
        new_due_date = request.form.get('due_date')
        if new_name:
            task_db.update(task_id, {'task_name': new_name, 'due_date': new_due_date})
            flash('Task updated successfully!', 'success')
            return redirect(url_for('tasks.home'))
    return render_template('edit_task.html', task=task)
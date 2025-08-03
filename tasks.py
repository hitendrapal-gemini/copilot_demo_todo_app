import json
import os
from flask import Blueprint, request, redirect, url_for, render_template, flash
from utils import generate_task_id  # Assuming this function is defined in utils.py
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
def home():
    tasks_data = task_db.list()
    return render_template('dashboard.html', tasks=tasks_data)

@tasks.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        task_id = generate_task_id()
        task = {
            'task_id': task_id,
            'task_name': task_name,
            'completed': False,
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
        flash(f'Task {task_description} marked as completed and email notification sent', 'success')
    else:
        flash('Task not found', 'danger')
    return redirect(url_for('tasks.home'))

@tasks.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    task_db.delete(task_id)
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.home'))
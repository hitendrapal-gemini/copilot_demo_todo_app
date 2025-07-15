# Description
This is a simple Todo app made in flask

# How to run locally
To run the app locally, run the below steps:

## Clone the repo
git clone https://github.com/hitendrapal-gemini/copilot_demo_todo_app.git

## Create virtual env
python -m venv .venv

## Install requirements
pip install -r requirements.txt

## Run main file
python app.py


# Prompts

## Add new feature - DueDate, Priority, assigned_to (Edits/Agent)

Update this Flask To‑Do app to support three new features for each task: 

1. A due_date field (date format), 

2. An assigned_to field (string – name or email of person assigned), 

3. A priority field (Low / Medium / High dropdown). 

Please update the below: 

1. The database model (models/tasks.py) to include these fields 

2. The form and template to allow users to input these fields when adding/editing a task 

3. The task list page to display these new fields 

Add validation: 

1. Priority is required – low by default 

2. Check on priority values (H/M/L) 

3. Date must be valid date

## Test Cases (Chat/Agent)

@workspace /tests - Generate exhaustive unit tests for the Flask routes in this file using pytest. Test cases should cover various edge cases like connection error, valid and invalid input, etc. Cover: 

1. Adding a new task 

2. Editing an existing task 

3. Deleting a task 

4. Viewing the task list 

Use appropriate fixtures, and mock the database where needed


## Documentation (Agent/Edit)

Add clear docstrings to all functions in this file using Google-style format. 
 Describe what each function does, its parameters, return values, and any important side effects.
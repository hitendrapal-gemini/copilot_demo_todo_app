# Project Overview

This project is a simple Todo application built using Flask. It allows users to add, view, complete, and delete tasks. The application is structured for easy extensibility and demonstration of prompt engineering techniques with GitHub Copilot.

## Codebase Structure

- **app.py**: Main Flask application entry point. Registers blueprints and configures the app.
- **tasks.py**: Contains the core logic for task management (add, complete, delete, list).
- **utils.py**: Utility functions (e.g., task ID generation).
- **config.py**: Configuration settings for the app (e.g., secret keys, AWS config).
- **templates/**: HTML templates for rendering the UI (not shown here).
- **doc/**: Documentation and workshop materials.

## High-Level Design

```architecture-beta
component User as "User (Browser)"
component FlaskApp as "Flask App (app.py)"
component TasksBP as "Tasks Blueprint (tasks.py)"
component TaskStorage as "Task Storage (In-Memory Dict / DynamoDB)"
component Utils as "Utils (utils.py)"
component Config as "Config (config.py)"
component Templates as "Templates (dashboard.html, etc.)"
component AWS as "AWS Services (DynamoDB, SNS)" <<future>>

User -> FlaskApp : HTTP Requests
FlaskApp -> TasksBP
TasksBP -> TaskStorage
TasksBP -> Utils
FlaskApp -> Config
FlaskApp -> Templates
TaskStorage -> JSON file (db.json)
```

**Legend:**
- Solid arrows: Main flow of requests and logic.
- Dashed arrow: Possible future integration with AWS services.

## Key Features

- Add, view, complete, and delete todo tasks.
- Modular structure for easy feature extension.
- Designed for prompt engineering workshops and Copilot demonstrations.

---

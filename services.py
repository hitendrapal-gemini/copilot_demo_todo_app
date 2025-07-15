class TaskService:
    """
    Service class for managing tasks in an in-memory dictionary keyed by task_id for fast lookup.

    Attributes:
        tasks (dict): Dictionary mapping task_id to task data dicts.
    """

    def __init__(self, tasks=None):
        """
        Initialize the TaskService with an optional tasks dictionary.

        Args:
            tasks (dict, optional): Dictionary mapping task_id to task data. If None, initializes empty.
        """
        if tasks is None:
            tasks = {}
        self.tasks = tasks

    def get_tasks(self):
        """
        Retrieve all tasks as a list.

        Returns:
            list: List of task dictionaries.
        """
        return list(self.tasks.values())

    def add_task(self, task_id, task_name):
        """
        Add a new task to the task dictionary.

        Args:
            task_id (str): Unique identifier for the task.
            task_name (str): Name or description of the task.
        """
        self.tasks[task_id] = {
            'task_id': task_id,
            'task_name': task_name,
            'completed': False,
        }

    def complete_task(self, task_id):
        """
        Mark a task as completed by its ID.

        Args:
            task_id (str): Unique identifier for the task to complete.

        Returns:
            dict or None: The updated task dictionary if found, else None.
        """
        task = self.tasks.get(task_id)
        if task:
            task['completed'] = True
            return task
        return None

    def delete_task(self, task_id):
        """
        Delete a task from the task dictionary by its ID.

        Args:
            task_id (str): Unique identifier for the task to delete.
        """
        self.tasks.pop(task_id, None)

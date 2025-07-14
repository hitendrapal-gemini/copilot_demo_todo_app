import uuid

def generate_task_id(task_dict):
    """
    Generate a new task ID just greater than the maximum task ID in the provided dictionary.
    """
    items = task_dict.get('Items', [])
    max_id = 0
    for task in items:
        tid = task.get('task_id', '')
        if tid.startswith('TASK-'):
            try:
                num = int(tid[5:])
                if num > max_id:
                    max_id = num
            except ValueError:
                continue
    return f"TASK-{max_id + 1}"

# No changes required for tags feature.
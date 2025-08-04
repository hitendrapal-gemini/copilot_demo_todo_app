import uuid

def generate_task_id(task_dict):
    """
    Generate a unique task ID in the format 'TASK-N', where N is one greater than the current max.
    """
    items = task_dict.get("Items", [])
    max_id = 0
    for item in items:
        tid = item.get("task_id", "")
        if tid.startswith("TASK-"):
            try:
                num = int(tid.split("-")[1])
                if num > max_id:
                    max_id = num
            except (IndexError, ValueError):
                continue
    return f"TASK-{max_id + 1}"
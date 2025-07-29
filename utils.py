
# Funtion to get a unique identifier for a task.
# New task ID just greater than the maximum task ID in the provided dictionary.
# Example 1:
# task_dict = {"Items": [{"task_id": "TASK-1, .."},.. {"task_id": "TASK-6, .."}]}
# task_id = generate_task_id(task_dict)  # Returns a "TASK-7"

# Example 2:
# task_dict = {"Items": [{"task_id": "TASK-78, .."},.. {"task_id": "TASK-99, .."}]}
# task_id = generate_task_id(task_dict)  # Returns a "TASK-100"

def generate_task_id(task_dict):
    if not task_dict['Items']:
        return 'TASK-1'
    
    max_id = 0
    for task in task_dict['Items']:
        task_id = task['task_id']
        if task_id.startswith('TASK-'):
            try:
                num = int(task_id.split('-')[1])
                if num > max_id:
                    max_id = num
            except ValueError:
                continue
    
    return f'TASK-{max_id + 1}'
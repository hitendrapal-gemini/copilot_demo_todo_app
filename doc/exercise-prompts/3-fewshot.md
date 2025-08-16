# 1.3 Few-Shot Prompting
**Goal:** Guide Copilot by providing examples.  
**detail**: Few-shot prompting means you provide one or more examples in your prompt to show Copilot the pattern or style you want. By demonstrating how to solve a similar problem, you help Copilot generalize and apply the same logic to new, related tasks. This is especially helpful for more complex or nuanced requirements.

## ❌ Bad Prompt Examples
```Funtion to get a unique identifier for a task```

## ✅ Good Prompt Examples
```
Funtion to get a unique identifier for a task.
New task ID just greater than the maximum task ID in the provided dictionary.
Example 1:
task_dict = {"Items": [{"task_id": "TASK-1, .."},.. {"task_id": "TASK-6, .."}]}
task_id = generate_task_id(task_dict)  # Returns a "TASK-7"

Example 2:
task_dict = {"Items": [{"task_id": "TASK-78, .."},.. {"task_id": "TASK-99, .."}]}
task_id = generate_task_id(task_dict)  # Returns a "TASK-100"

Also change the usage of generate_task_id in the code
```

## Demo (on `module-3-base` branch)
- **Task:** Change the format of the Task ID.
- **Prompt:** 
```Funtion to get a unique identifier for a task.
New task ID just greater than the maximum task ID in the provided dictionary.
Example 1:
task_dict = {"Items": [{"task_id": "TASK-1, .."},.. {"task_id": "TASK-6, .."}]}
task_id = generate_task_id(task_dict)  # Returns a "TASK-7"

Example 2:
task_dict = {"Items": [{"task_id": "TASK-78, .."},.. {"task_id": "TASK-99, .."}]}
task_id = generate_task_id(task_dict)  # Returns a "TASK-100"
```
- **Fix Error Prompt:**
```
fix the error

File "/Users/tarindersingh/gemini/copilot_demo_todo_app/tasks.py", line 71, in add_task
task_id = generate_task_id()
TypeError: generate_task_id() missing 1 required positional argument: 'task_dict'
```

## Reflective Questions
- How does providing an example change Copilot’s output?
- What if the example is too complex or not relevant?
- How would you improve the example?

## Learn More
- [Few-Shot Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#few-shot)

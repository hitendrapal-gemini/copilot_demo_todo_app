# Prompting Techniques for Software Developers: Code Generation in a To-Do App

This presentation covers key prompt engineering techniques for software developers, using code generation for a To-Do app as the context. Each technique includes:
- Purpose
- Prompt Format
- Example Prompt
- Example Output
- Best to use this technique
- Must avoid to use this technique
- Showcasing Bad vs. Good
- Flawed prompt for audience debugging
- Explanation of issues in the flawed prompt

---

## 1. 4S Technique (Single, Specific, Short, Surround)

**Purpose:**
Craft prompts that are focused, clear, concise, and provide enough context for accurate code generation.

**Prompt Format:**
```
[Single, Specific, Short instruction]
// Surround with context or comments if needed
```

**Example Prompt:**
```
Add a due date field to each todo item. // Add field to model // Update form // Show in dashboard
```

**Example Output:**
```python
# Add due_date field to Todo model
class Todo(db.Model):
    # ...existing code...
    due_date = db.Column(db.Date)
    # ...existing code...

# Update add task form and dashboard template accordingly
```

**Best to use this technique:**
When you want to minimize ambiguity and maximize clarity for simple or multi-step tasks.

**Must avoid to use this technique:**
When the task is inherently complex and needs more detailed breakdown or examples.

**Showcasing Bad vs. Good:**
| Principle | ❌ Bad Prompt | ✅ Good Prompt |
|-----------|--------------|---------------|
| **Single** | "Add due date and priority to tasks." | "Add a due date field to each todo item." |
| **Specific** | "Improve the dashboard." | "Display each todo item's due date in the dashboard table." |
| **Short** | "Can you please update the code so that every time a user adds a new task, the app will also ask for a due date and then show that due date in the dashboard view?" | "Add a due date field to the add task form and show it in the dashboard." |
| **Surround** | "Add a due date." | "Add a due date field to each todo item. // Add field to model // Update form // Show in dashboard" |

---

## 2. Zero-Shot Prompting

**Purpose:**
Use for direct, simple code generation tasks where the model is expected to infer the task from the instruction alone.

**Prompt Format:**
```
[Instruction]
```

**Example Prompt:**
```
Write a function in Python to add a new task to a to-do list.
```

**Example Output:**
```
def add_task(todo_list, task):
    todo_list.append(task)
```

**Best to use this technique:**
When the task is simple, unambiguous, and widely understood.

**Must avoid to use this technique:**
When the task is complex, ambiguous, or requires specific style, reasoning, or context.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Write code for task add.
- **Good Prompt:**
  Write a Python function that to add string task to a list called `todo_list`.

---

## 3. Few-Shot Prompting

**Purpose:**
Guide the model’s response by providing a few input-output code examples before the main user query.

**Prompt Format:**
```
User: [Example Input 1]
Assistant: [Example Output 1]

User: [Example Input 2]
Assistant: [Example Output 2]

User: [Actual Input]
Assistant:
```

**Example Prompt:**
```
User: Write a function to delete a task from a to-do list in Python.
Assistant: def delete_task(todo_list, task):
    todo_list.remove(task)

User: Write a function to mark a task as complete in a to-do list (Python).
Assistant: def complete_task(todo_list, task):
    if task in todo_list:
        todo_list[todo_list.index(task)] += ' (done)'

User: Write a function to list all tasks in a to-do list.
Assistant:
```

**Example Output:**
```
def list_tasks(todo_list):
    for task in todo_list:
        print(task)
```

**Best to use this technique:**
When you want consistent output style or the task may be ambiguous.

**Must avoid to use this technique:**
When the task is very simple or when providing examples may bias the output undesirably.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  List tasks.
- **Good Prompt:**
  Write a Python function that prints each task in a list called `todo_list`.

---

## 4. Chain-of-Thought (CoT) Prompting

**Purpose:**
Encourage the model to reason through multi-step code generation or logic for more accurate results.

**Prompt Format:**
```
Let's think step by step.
[Task description or scenario]
```

**Example Prompt:**
```
Let's think step by step.
I want to create a function that adds a task to a to-do list only if it doesn't already exist. How should I do this in Python?
```

**Example Output:**
```
1. First, check if the task is already in the list.
2. If not, append the task.
3. Otherwise, do nothing.

Code:
def add_unique_task(todo_list, task):
    if task not in todo_list:
        todo_list.append(task)
```

**Best to use this technique:**
When the task requires reasoning, validation, or multi-step logic.

**Must avoid to use this technique:**
When the task is straightforward and does not require step-by-step reasoning.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Add a task if needed.
- **Good Prompt:**
  Write a Python function that adds a task to a list only if it is not already present.

**Flawed prompt to be debugged by audience:**
```
Make sure tasks are not repeated.
```

**Explain issues in Flawed prompt:**
- No code context or language.
- No data structure specified.
- Lacks step-by-step reasoning.

---

## 5. Mega Prompt

**Purpose:**
Provide extensive context, instructions, and examples for complex or multi-capability code generation tasks.

**Prompt Format:**
```
You are [role/context].
The app allows users to:
- [Capability 1]
- [Capability 2]
[Style/Output guidance]

Example Input: [Sample input]
Example Output: [Sample output]

User Input: [Actual input]
```

**Example Prompt:**
```
You are an expert Python developer.
The to-do app allows users to:
- Add, delete, and complete tasks
- Set deadlines and priorities
Respond with clean, well-documented code.

Example Input: Write a function to add a task with a deadline.
Example Output: def add_task(todo_list, task, deadline):
    todo_list.append({'task': task, 'deadline': deadline})

User Input: Write a function to mark a task as high priority.
```

**Example Output:**
```
def mark_high_priority(todo_list, task):
    for t in todo_list:
        if t['task'] == task:
            t['priority'] = 'high'
```

**Best to use this technique:**
For complex, multi-capability code generation or when style/format consistency is required.

**Must avoid to use this technique:**
When the task is simple or when brevity and speed are more important than completeness.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Make a to-do app.
- **Good Prompt:**
  Write a Python class for a to-do app with methods to add, delete, and mark tasks as complete.

**Flawed prompt to be debugged by audience:**
```
I want everything for a to-do app.
```

**Explain issues in Flawed prompt:**
- Overly broad and unspecific.
- No language, structure, or features detailed.
- No examples or style guidance.

---

## 6. Adaptive Prompt

**Purpose:**
Adjust the prompt based on prior user actions or evolving context for dynamic, multi-turn code generation.

**Prompt Format:**
```
Based on the following completed tasks:
- [Completed Task 1]
- [Completed Task 2]

And these remaining tasks:
- [Remaining Task 1] ([Deadline/priority])
- [Remaining Task 2] ([Deadline/priority])

[Instruction for next action]
```

**Example Prompt:**
```
Based on the following completed features:
- Add task function
- Delete task function

And these remaining features:
- Mark task as complete (high priority)
- List all tasks (medium priority)

Write the next function, focusing on the highest priority.
```

**Example Output:**
```
def complete_task(todo_list, task):
    if task in todo_list:
        todo_list[todo_list.index(task)] += ' (done)'
```

**Best to use this technique:**
For multi-turn, context-sensitive code generation where requirements evolve.

**Must avoid to use this technique:**
When there is no prior context or when a single, isolated task is required.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Write another function.
- **Good Prompt:**
  Based on the completed add and delete functions, write a Python function to mark a task as complete.

**Flawed prompt to be debugged by audience:**
```
Keep going.
```

**Explain issues in Flawed prompt:**
- No context or direction.
- No indication of what has been done or what is needed next.

---

## 7. Roleplay Prompt

**Purpose:**
Assign the model a persona or role to shape the tone, style, or expertise of the code response.

**Prompt Format:**
```
Act as a [role/persona].
Here are my tasks:
- [Task 1]
- [Task 2]
[Role-specific instruction]
```

**Example Prompt:**
```
Act as a senior Python engineer.
Here are my requirements:
- Add tasks
- Delete tasks
- Mark tasks as complete
Write a class that implements these features with docstrings.
```

**Example Output:**
```
class TodoApp:
    """A simple to-do app."""
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, task):
        self.tasks.remove(task)
    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[self.tasks.index(task)] += ' (done)'
```

**Best to use this technique:**
When a specific communication style, expertise, or persona is needed in code generation.

**Must avoid to use this technique:**
When the role or persona is irrelevant to the task or may introduce unnecessary complexity.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Make a class.
- **Good Prompt:**
  Act as a senior Python engineer and write a class for a to-do app with add, delete, and complete methods.

**Flawed prompt to be debugged by audience:**
```
Do it like an expert.
```

**Explain issues in Flawed prompt:**
- No details on what "it" is.
- No requirements or context.
- No language or structure guidance.

---

## 8. Multimodal Prompt

**Purpose:**
Enable the model to process and reason with both text and images for richer, more flexible code generation input.

**Prompt Format:**
```
You are a code assistant that can process images and text.
The user has uploaded an image of handwritten requirements for a to-do app.

Instructions:
1. Extract the requirements from the image.
2. Write Python code to implement them.
```

**Example Prompt:**
```
[Image: Photo of handwritten requirements]
```

**Example Output:**
```
Extracted requirements:
- Add task
- Delete task
- List tasks

Python code:
def add_task(todo_list, task):
    todo_list.append(task)
def delete_task(todo_list, task):
    todo_list.remove(task)
def list_tasks(todo_list):
    for task in todo_list:
        print(task)
```

**Best to use this technique:**
When combining visual and textual information for code generation.

**Must avoid to use this technique:**
When only text input is available or when image processing is not needed for the task.

**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Here’s a picture.
- **Good Prompt:**
  Here’s a photo of my to-do app requirements. Extract the features and write Python functions for each.

**Flawed prompt to be debugged by audience:**
```
Look at this and code.
```

**Explain issues in Flawed prompt:**
- No description of what to extract or code.
- No language or output format guidance.

---

## 9. Hallucination Handling

**Purpose:**
Reduce the risk of the model generating plausible but incorrect or fabricated code (hallucinations) by explicitly instructing it to verify, cite, or limit its output to known information.

**Prompt Format:**
```
[Instruction with verification/citation request]
```

**Example Prompt:**
```
Write a Python function to add a task to a to-do list. If you are unsure about any part, say "I don't know" or ask for clarification.
```

**Example Output:**
```
def add_task(todo_list, task):
    todo_list.append(task)
# If you want to handle duplicates, please specify.
```

**Best to use this technique:**
When accuracy is critical, or when the model may be prone to making up details.


**Showcasing Bad vs. Good:**
- **Bad Prompt:**
  Write a function to do something with tasks.
- **Good Prompt:**
  Write a Python function to add a task to a list. If you are unsure about any requirement, ask for clarification instead of guessing.

---

# Final Tips for Prompt Engineering in Code Generation
- Start simple (zero-shot), escalate as complexity grows.
- Be explicit about output format and expectations.
- Use examples (few-shot/mega) when consistency or style matters.
- Iterate and test—improve prompts based on observed outputs.
- Document successful prompts for future reference.


# Summary Table

| Technique         | Purpose                                   | Format Example                                     | Best For                          |
|-------------------|-------------------------------------------|----------------------------------------------------|------------------------------------|
| 4S Technique      | Focused, clear, concise prompts          | "[Single, Specific, Short instruction] // ..."    | Minimizing ambiguity, simple tasks |
| Zero-Shot         | Direct, simple tasks                      | "[Instruction]"                                    | Simple, unambiguous requests       |
| Few-Shot          | Style/output consistency                  | "User: ... Assistant: ... (examples)"              | Tasks needing format/style mimicry |
| Chain-of-Thought  | Reasoning, prioritization                 | "Let's think step by step. [Scenario]"             | Multi-step reasoning               |
| Mega Prompt       | Complex/multi-capability tasks            | "[Role/rules/examples] User Input: ..."            | Complex, context-rich scenarios    |
| Adaptive          | Multi-turn, context-sensitive interaction | "[Based on completed/remaining tasks: ...]"        | Dynamic, evolving conversations    |
| Roleplay          | Persona-driven engagement                 | "Act as a [role]... [Tasks] [Instruction]"         | Specialized tone/style             |
| Multimodal        | Image+text scenarios                      | "[Instructions] [Image]"                           | Combining visual and textual info  |
| Hallucination Handling | Reducing incorrect or fabricated code | "[Instruction with verification/citation request]" | Ensuring accuracy, handling uncertainty |

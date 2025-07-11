# GitHub Copilot Prompt Engineering Workshop Roadmap  
**Base Project:** Flask Todo App  
**Audience:** Software Developers  
**Format:** 7–8 min per segment, hands-on, branch-per-concept

---

## 1. Foundational Prompting Techniques

### 1.1 The 4S Principle (Single, Specific, Short, Surround)
**Goal:** Learn to craft prompts that are clear and actionable.  
**detail**: The 4S Principle stands for Single, Specific, Short, and Surround. It encourages you to write prompts that focus on one task (Single), are unambiguous (Specific), use concise language (Short), and provide enough context or code comments (Surround) to guide Copilot effectively. This approach reduces misunderstandings and increases the quality of Copilot’s suggestions.

#### 4S Breakdown with Examples

| Principle | ❌ Bad Prompt | ✅ Good Prompt |
|-----------|--------------|---------------|
| **Single** | "Add due date and priority to tasks." | "Add a due date field to each todo item." |
| **Specific** | "Improve the dashboard." | "Display each todo item's due date in the dashboard table." |
| **Short** | "Can you please update the code so that every time a user adds a new task, the app will also ask for a due date and then show that due date in the dashboard view?" | "Add a due date field to the add task form and show it in the dashboard." |
| **Surround** | "Add a due date." | "Add a due date field to each todo item. // Add field to model // Update form // Show in dashboard" |

#### Demo (on `module-3-prompting` branch)
- **Task:** Add a due date to each todo item.
- **Prompt:**  
  *"Add a due date field to each todo item in the Flask app. Update the add task form, backend logic, and dashboard template to support this."*

#### Reflective Questions
- What might go wrong if the prompt is too vague?
- How would you improve a prompt that’s too long or tries to do too much?
- If we only say “add due date,” what might Copilot miss?

#### Learn More
- [GitHub Copilot Prompting Guide](https://docs.github.com/en/copilot/using-github-copilot/getting-github-copilot-to-suggest-better-code)
- [Prompt Engineering Patterns](https://promptingguide.ai/)

---

### 1.2 Zero-Shot Prompting
**Goal:** Use Copilot with a single, clear instruction—no examples.  
**detail**: Zero-shot prompting involves giving Copilot a direct, standalone instruction without any examples or demonstrations. The model relies solely on the clarity and completeness of your prompt. This technique is useful for straightforward tasks but requires you to be precise to avoid ambiguity or misinterpretation.

#### ❌ Bad Prompt Examples
- "Don't allow past dates."
- "Let users change tasks."
- "Add some validation to the form."
- "Make tasks editable."

#### ✅ Good Prompt Examples
- "Ensure that the due date selected for a new task cannot be in the past. Only allow today or future dates in the add task form."
- "Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard."
- "Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard. Style the Edit button with a yellow background color, similar to how the Complete button is blue and the Delete button is red."

#### Demo (on `module-3-prompting` branch)
- **Task 1:** Prevent users from selecting a past date as the due date.
  - **Prompt:**  
    *"Ensure that the due date selected for a new task cannot be in the past. Only allow today or future dates in the add task form."*
- **Task 2:** Allow users to edit tasks.
  - **Prompt:**  
    *"Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard."*
  - **Improved Prompt:**  
    *"Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard. Style the Edit button with a yellow background color, similar to how the Complete button is blue and the Delete button is red."*


#### Reflective Questions
- What might Copilot misunderstand in a zero-shot prompt?
- How would you clarify intent if Copilot’s output is off?
- If we change “edit” to “update only the due date,” what would you expect?

#### Learn More
- [Zero-Shot Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#zero-shot)

---

### 1.3 Few-Shot Prompting
**Goal:** Guide Copilot by providing examples.  
**detail**: Few-shot prompting means you provide one or more examples in your prompt to show Copilot the pattern or style you want. By demonstrating how to solve a similar problem, you help Copilot generalize and apply the same logic to new, related tasks. This is especially helpful for more complex or nuanced requirements.

#### ❌ Bad Prompt Examples
```Funtion to get a unique identifier for a task```

#### ✅ Good Prompt Examples
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

#### Demo (on `module-3-prompting` branch)
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
Fix the error

Traceback (most recent call last):
  File "C:\Users\Tarinder.Singh\projects\copilot_demo_todo_app\app.py", line 2, in <module>
    from tasks import tasks 
    ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Tarinder.Singh\projects\copilot_demo_todo_app\tasks.py", line 39
    global TASK_DICT
    ^^^^^^^^^^^^^^^^
SyntaxError: name 'TASK_DICT' is used prior to global declaration
```

#### Reflective Questions
- How does providing an example change Copilot’s output?
- What if the example is too complex or not relevant?
- How would you improve the example?

#### Learn More
- [Few-Shot Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#few-shot)

---

## 2. Handling Copilot Limitations

### 2.1 Hallucination Handling
**Goal:** Detect and mitigate Copilot’s “hallucinations” (confident but incorrect code).  
**detail**: Hallucination handling is about recognizing when Copilot generates code that looks plausible but is actually incorrect or based on false assumptions. By asking Copilot to explain its reasoning, list assumptions, or reference dependencies, you can catch and correct these errors before they cause issues in your codebase.

#### ❌ Bad Prompt Examples
- "Add email notification when a task is completed." (without checking if email config exists)

#### ✅ Good Prompt Examples
- "Add email notification when a task is completed. Explain your reasoning and list any assumptions about configuration or dependencies."

#### Demo (on `feature/hallucination-handling` branch)
- **Task:** Add email notification on task completion.
- **Prompt:**  
  *"Add code to send an email notification when a task is marked as completed. Explain your reasoning and any assumptions about configuration or libraries."*

#### Reflective Questions
- What might go wrong if Copilot assumes a library or config exists?
- How would you verify Copilot’s reasoning?
- What if Copilot “hallucinates” a function that doesn’t exist?

#### Learn More
- [Copilot Limitations](https://docs.github.com/en/copilot/using-github-copilot/getting-github-copilot-to-suggest-better-code#copilot-limitations)
- [AI Hallucinations](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))

---

## 3. Advanced Prompting Techniques

### 3.1 Chain-of-Thought Prompting
**Goal:** Guide Copilot to reason step-by-step.  
**detail**: Chain-of-thought prompting breaks down a complex task into a sequence of smaller, logical steps. By explicitly listing each step in your prompt, you help Copilot follow a clear path to the solution, improving accuracy and making the generated code easier to understand and debug.

#### ❌ Bad Prompt Examples
- "Add a search feature."

#### ✅ Good Prompt Examples
- "Let’s add a search feature step by step:
  1. Add a search input to the dashboard.
  2. Filter tasks based on the search query.
  3. Display only matching tasks."

#### Demo (on `feature/chain-of-thought` branch)
- **Task:** Add search functionality.
- **Prompt:**  
  *"Step 1: Add a search input box to the dashboard. Step 2: Filter the displayed tasks based on the search query. Step 3: Show only tasks that match the query."*

#### Reflective Questions
- How does breaking down the task help Copilot?
- What if you skip a step?
- How would you chain more complex logic?

#### Learn More
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)

---

### 3.2 Mega-Prompts
**Goal:** Use detailed, multi-part prompts for complex features.  
**detail**: Mega-prompts are comprehensive instructions that cover multiple requirements or sub-tasks in a single prompt. They are useful for implementing complex features but can risk overwhelming Copilot or causing it to miss details. Structuring your mega-prompt clearly and logically helps Copilot deliver more complete solutions.

#### ❌ Bad Prompt Examples
- "Add user authentication."

#### ✅ Good Prompt Examples
- "Add user authentication to the Flask app:
  - Use Flask-Login.
  - Add login and logout routes.
  - Protect the dashboard so only logged-in users can access it.
  - Show the logged-in user’s name in the navbar."

#### Demo (on `feature/mega-prompt` branch)
- **Task:** Add authentication.
- **Prompt:**  
  *"Add user authentication using Flask-Login. Implement login/logout routes, protect the dashboard, and display the user’s name in the navbar."*

#### Reflective Questions
- What are the risks of very long prompts?
- How might Copilot miss or misinterpret parts?
- How would you split a mega-prompt into smaller steps?

#### Learn More
- [Prompt Engineering Patterns](https://promptingguide.ai/)

---

### 3.3 Adaptive Prompting / Self-Refinement
**Goal:** Iteratively refine prompts based on Copilot’s output.  
**detail**: Adaptive prompting is an iterative process where you review Copilot’s output, identify gaps or errors, and adjust your prompt to improve results. You can also ask Copilot to critique or refine its own suggestions, leading to higher-quality code through self-refinement.

#### ❌ Bad Prompt Examples
- "Fix the bug."

#### ✅ Good Prompt Examples
- "The delete button sometimes doesn’t work. First, explain what might be wrong. Then, suggest a fix and explain your reasoning."

#### Demo (on `feature/adaptive-prompting` branch)
- **Task:** Debug the delete button.
- **Prompt:**  
  *"The delete button on the dashboard sometimes fails. First, explain possible causes. Then, suggest a fix and explain your reasoning."*

#### Reflective Questions
- How do you adapt your prompt after seeing Copilot’s output?
- What if Copilot’s explanation is wrong?
- How would you ask Copilot to self-refine?

#### Learn More
- [Self-Refinement in LLMs](https://arxiv.org/abs/2303.17651)

---

### 3.4 Multimodal Prompting
**Goal:** Use code, comments, and UI context to guide Copilot.  
**detail**: Multimodal prompting involves providing Copilot with multiple types of context—such as code snippets, comments, UI descriptions, or file references—to guide its suggestions. This technique is especially effective for tasks that span different layers of your application, like updating both backend logic and frontend UI.

#### ❌ Bad Prompt Examples
- "Make the UI look better."

#### ✅ Good Prompt Examples
- "Update the dashboard.html and style.css to make the task list more visually appealing. Add a hover effect to each task item and improve the color scheme."

#### Demo (on `feature/multimodal-prompting` branch)
- **Task:** Improve UI.
- **Prompt:**  
  *"Update dashboard.html and style.css to add a hover effect to each task item and use a modern color palette."*

#### Reflective Questions
- How does including both code and UI context help Copilot?
- What if you only update one file?
- How would you describe a visual change in a prompt?

#### Learn More
- [Multimodal Prompting](https://platform.openai.com/docs/guides/multimodal)

---

### 3.5 Role-Play Prompting
**Goal:** Ask Copilot to act as a specific role (e.g., code reviewer, security expert).  
**detail**: Role-play prompting instructs Copilot to take on a particular persona or expertise, such as a security auditor or code reviewer. This can help you get more targeted feedback, uncover issues you might miss, or receive suggestions from a specific perspective.

#### ❌ Bad Prompt Examples
- "Check my code."

#### ✅ Good Prompt Examples
- "Act as a security expert. Review the Flask app for common security issues and suggest improvements."

#### Demo (on `feature/role-play-prompting` branch)
- **Task:** Security review.
- **Prompt:**  
  *"Act as a security expert. Review the Flask app for vulnerabilities such as XSS, CSRF, and insecure secrets. Suggest code changes to improve security."*

#### Reflective Questions
- How does role-play change Copilot’s output?
- What if you ask Copilot to act as a beginner?
- How would you combine role-play with other techniques?

#### Learn More
- [Role Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#role-prompting)

---

## Workshop Wrap-Up

- **Practice:** Try each technique on a new feature or bug.
- **Reflect:** Which prompting style worked best for you? Why?
- **Limitations:**  
  - Copilot’s context window is limited—large files or projects may reduce accuracy.
  - Hallucinations: Always review and test Copilot’s output.
  - Copilot may misunderstand intent—iterate and clarify as needed.

---

**Next Steps:**  
- Experiment with your own prompts.
- Share your best (and worst) prompts with the group.
- Explore the “Learn More” links for deeper mastery.

---

**Happy Prompting!**  
*Branch after each segment: `feature/<technique>`*

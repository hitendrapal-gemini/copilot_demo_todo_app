# 1.1 The 4S Principle (Single, Specific, Short, Surround)
**Goal:** Learn to craft prompts that are clear and actionable.  
**detail**: The 4S Principle stands for Single, Specific, Short, and Surround. It encourages you to write prompts that focus on one task (Single), are unambiguous (Specific), use concise language (Short), and provide enough context or code comments (Surround) to guide Copilot effectively. This approach reduces misunderstandings and increases the quality of Copilot’s suggestions.

## 4S Breakdown with Examples

| Principle | ❌ Bad Prompt | ✅ Good Prompt |
|-----------|--------------|---------------|
| **Single** | "Add due date and priority to tasks." | "Add a due date field to each todo item." |
| **Specific** | "Improve the dashboard." | "Display each todo item's due date in the dashboard table." |
| **Short** | "Can you please update the code so that every time a user adds a new task, the app will also ask for a due date and then show that due date in the dashboard view?" | "Add a due date field to the add task form and show it in the dashboard." |
| **Surround** | "Add a due date." | "Add a due date field to each todo item. // Add field to model // Update form // Show in dashboard" |

## Demo (on `module-3-base` branch)
- **Task:** Add a due date to each todo item.
- **Prompt:**  
  *"Add a due date field to each todo item in the Flask app. Update the add task form, backend logic, and dashboard template to support this."*

## Reflective Questions
- What might go wrong if the prompt is too vague?
- How would you improve a prompt that’s too long or tries to do too much?
- If we only say “add due date,” what might Copilot miss?

## Learn More
- [GitHub Copilot Prompting Guide](https://docs.github.com/en/copilot/using-github-copilot/getting-github-copilot-to-suggest-better-code)
- [Prompt Engineering Patterns](https://promptingguide.ai/)

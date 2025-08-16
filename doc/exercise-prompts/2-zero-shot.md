# 1.2 Zero-Shot Prompting
**Goal:** Use Copilot with a single, clear instruction—no examples.  
**detail**: Zero-shot prompting involves giving Copilot a direct, standalone instruction without any examples or demonstrations. The model relies solely on the clarity and completeness of your prompt. This technique is useful for straightforward tasks but requires you to be precise to avoid ambiguity or misinterpretation.

## ❌ Bad Prompt Examples
- "Don't allow past dates."
- "Let users change tasks."
- "Add some validation to the form."
- "Make tasks editable."

## ✅ Good Prompt Examples
- "Ensure that the due date selected for a new task cannot be in the past. Only allow today or future dates in the add task form."
- "Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard."
- "Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard. Style the Edit button with a yellow background color, similar to how the Complete button is blue and the Delete button is red."

## Demo (on `module-3-base` branch)
- **Task 1:** Prevent users from selecting a past date as the due date.
  - **Prompt:**  
    *"Ensure that the due date selected for a new task cannot be in the past. Only allow today or future dates in the add task form."*
- **Task 2:** Allow users to edit tasks.
  - **Prompt:**  
    *"Add a feature to allow users to edit the name and due date of an existing todo item directly from the dashboard. Style the Edit button with a yellow background color"*


## Reflective Questions
- What might Copilot misunderstand in a zero-shot prompt?
- How would you clarify intent if Copilot’s output is off?
- If we change “edit” to “update only the due date,” what would you expect?

## Learn More
- [Zero-Shot Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#zero-shot)
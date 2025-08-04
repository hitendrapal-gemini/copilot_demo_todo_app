### 3.2 Mega-Prompts
**Goal:** Use detailed, multi-part prompts for complex features.  
**detail**: Mega-prompts are comprehensive instructions that cover multiple requirements or sub-tasks in a single prompt. They are useful for implementing complex features but can risk overwhelming Copilot or causing it to miss details. Structuring your mega-prompt clearly and logically helps Copilot deliver more complete solutions.

#### ❌ Bad Prompt Examples
- "Add user authentication."

#### ✅ Good Prompt Examples
- "#codebase Add user authentication to the Flask app:
  - Use Flask-Login.
  - Add login and logout routes.
  - Protect the dashboard so only logged-in users can access it.
  - Show the logged-in user’s name in the navbar."

#### Demo (on `module-5-prompting` branch)
- **Task:** Add authentication.
- **Prompt:**  
  *" #codebase Add user authentication using Flask-Login. Implement login/logout routes, protect the dashboard, and display the user’s name in the navbar."*

#### Reflective Questions
- What are the risks of very long prompts?
- How might Copilot miss or misinterpret parts?
- How would you split a mega-prompt into smaller steps?

#### Learn More
- [Prompt Engineering Patterns](https://promptingguide.ai/)
### 3.5 Multimodal Prompting
**Goal:** Use code, comments, and UI context to guide Copilot.  
**detail**: Multimodal prompting involves providing Copilot with multiple types of context—such as code snippets, comments, UI descriptions, or file references—to guide its suggestions. This technique is especially effective for tasks that span different layers of your application, like updating both backend logic and frontend UI.

#### ❌ Bad Prompt Examples
- "Make the UI look better."

#### ✅ Good Prompt Examples
- "Update the dashboard.html and style.css to make the task list more visually appealing. Add a hover effect to each task item and improve the color scheme."

#### Demo (on `module-5-prompting` branch)
- **Task:** Improve UI.
- **Prompt:**  
  *"Update dashboard.html and style.css to add a hover effect to each task item and use a modern color palette."*

#### Reflective Questions
- How does including both code and UI context help Copilot?
- What if you only update one file?
- How would you describe a visual change in a prompt?

#### Learn More
- [Multimodal Prompting](https://platform.openai.com/docs/guides/multimodal)
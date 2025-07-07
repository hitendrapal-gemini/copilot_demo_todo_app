# GitHub Copilot Prompt Engineering Workshop Roadmap  
**Base Project:** Flask Todo App  
**Audience:** Software Developers  
**Format:** 7–8 min per segment, hands-on, branch-per-concept

---

## 1. Foundational Prompting Techniques

### 1.1 The 4S Principle (Single, Specific, Short, Surround)
**Goal:** Learn to craft prompts that are clear and actionable.

#### ❌ Bad Prompt Examples
- "Add a feature."
- "Make the app better."

#### ✅ Good Prompt Examples
- "Add a due date field to each todo item and display it in the dashboard."
- "Surround the code for adding a new task with comments explaining each step."

#### Demo (on `feature/4s-principle` branch)
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

#### ❌ Bad Prompt Examples
- "Make tasks deletable."
- "Add notifications."

#### ✅ Good Prompt Examples
- "Implement a delete button for each todo item in the dashboard. When clicked, remove the item from the list and update the UI."
- "Send a flash message when a task is marked as completed."

#### Demo (on `feature/zero-shot-prompting` branch)
- **Task:** Add a delete button to each todo item.
- **Prompt:**  
  *"Add a delete button next to each todo item in the dashboard. When clicked, remove the item from the list and show a flash message."*

#### Reflective Questions
- What might Copilot misunderstand in a zero-shot prompt?
- How would you clarify intent if Copilot’s output is off?
- If we change “delete” to “archive,” what would you expect?

#### Learn More
- [Zero-Shot Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#zero-shot)

---

### 1.3 Few-Shot Prompting
**Goal:** Guide Copilot by providing examples.

#### ❌ Bad Prompt Examples
- "Add another feature like marking tasks as important."

#### ✅ Good Prompt Examples
- "Here’s how to add a completed status to a task:
  1. Add a 'completed' field to the task.
  2. Update the UI to show completed tasks.
  Now, add an 'important' field to each task and display it with a star icon if set."

#### Demo (on `feature/few-shot-prompting` branch)
- **Task:** Add an “important” flag to tasks.
- **Prompt:**  
  *"Example: To add a completed status, we added a 'completed' field and updated the UI. Now, add an 'important' field to each task and show a star icon for important tasks."*

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
*Branch after each segment: `feature/<technique
### 2.1 Hallucination Handling

**Goal:** Detect and mitigate Copilot’s “hallucinations” (confident but incorrect code).  
**detail**: Hallucination handling is about recognizing when Copilot generates code that looks plausible but is actually incorrect or based on false assumptions. By asking Copilot to explain its reasoning, list assumptions, or reference dependencies, you can catch and correct these errors before they cause issues in your codebase.

#### ❌ Bad Prompt Examples
- "Add email notification when a task is completed." (without checking if email config exists)

#### ✅ Good Prompt Examples
- "Add email notification when a task is completed. Explain your reasoning and list any assumptions about configuration or dependencies."

#### Demo (on `module-3-base` branch)
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

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

#### Demo (on `module-3-base` branch)
- **Task:** Add search functionality.
- **Prompt:**  
  *" Add search functionality as mentioned below
    Step 1: Add a search input box to the dashboard. 
    Step 2: Filter the displayed tasks based on the search query.
    Step 3: Show only tasks that match the query."*

#### Reflective Questions
- How does breaking down the task help Copilot?
- What if you skip a step?
- How would you chain more complex logic?

#### Learn More
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
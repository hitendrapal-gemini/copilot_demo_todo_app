### 3.3 Adaptive Prompting / Self-Refinement
**Goal:** Iteratively refine prompts based on Copilot’s output.  
**detail**: Adaptive prompting is an iterative process where you review Copilot’s output, identify gaps or errors, and adjust your prompt to improve results. You can also ask Copilot to critique or refine its own suggestions, leading to higher-quality code through self-refinement.

#### ❌ Bad Prompt Examples
- "Add "Tags" feature for each todo item, users should be able to assign multiple tags."

#### ✅ Good Prompt Examples
- "Add "Tags" feature for each todo item. Users should be able to assign multiple tags to a single todo. How should I approach this?"

#### Demo (on `module-3-base` branch)
- **Task:** Add "Tags" feature for each todo item.
- **Ask Initial Prompt:**  
"@workspace Add "Tags" feature for each todo item. Users should be able to assign multiple tags to a single todo. How should I approach this?"
- **Refine Prompt:**
"When adding/editing a todo, what's the best way for users to input multiple tags? Should it be a text input with auto-suggestion, checkboxes, or a multi-select dropdown?"
- **Edit Final Prompt:**
"#codebase Add "Tags" feature for each todo item. Users should be able to assign multiple tags to a single todo. Use a multi-select dropdown with auto-suggestion (e.g., Select2 or Bootstrap Tags Input)"


#### Reflective Questions
- How do you adapt your prompt after seeing Copilot’s output?
- What if Copilot’s explanation is wrong?
- How would you ask Copilot to self-refine?

#### Learn More
- [Self-Refinement in LLMs](https://arxiv.org/abs/2303.17651)
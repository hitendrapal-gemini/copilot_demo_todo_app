# 🧠 GitHub Copilot Prompt Engineering – Summary

## 1. Structure
- The Prompt Engineering is divided into two modules:
  - **Core Techniques**
  - **Advanced Prompting**

## 2. Format
- Each concept is taught in a 7–8 minute hands-on segment.
- We use a **Flask Todo App** as the base project.
- Each module is demonstrated on a separate Git branch.
- Each technique has Good and Bad prompts.

## 3. Demo-Driven Learning
- For every prompting style, we implement a **real feature** in the Todo app and run it locally.

---

## 🧩 Module 1: Core Techniques

### 🔹 4S Principle *(Single, Specific, Short, Surround)*
- **Feature**: Add a **due date** field to each todo item.

### 🔹 Zero-Shot Prompting
- **Feature**: Prevent **past due dates** and allow **task editing**.

### 🔹 Few-Shot Prompting
- **Feature**: Generate a **unique task ID** using examples.

### 🔹 Hallucination Handling
- **Feature**: Add **email notifications** when a task is completed, while asking Copilot to explain its assumptions and reasoning.

---

## 🚀 Module 2: Advanced Prompting
### 🔹 Chain-of-Thought Prompting
- **Feature**: Implement **search functionality** step-by-step.

### 🔹 Mega-Prompts
- **Feature**: Add **user authentication** with multiple sub-tasks.

### 🔹 Adaptive Prompting / Self-Refinement
- **Feature**: Add **tags** to todos using iterative refinement.

### 🔹 Role-Play Prompting
- **Feature**: Conduct a **security review** as a security expert.

### 🔹 Multimodal Prompting
- **Feature**: Improve **UI styling** using HTML and CSS context.

---

## ✅ Wrap-Up
- Practice each technique on a new feature or bug.
- Reflect on which prompting style worked best for you and why.
- Discuss limitations like Copilot’s context window and hallucinations.
- Share your best and worst prompts with the group.
- Explore linked resources for deeper mastery


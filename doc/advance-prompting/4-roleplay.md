### 3.4 Role-Play Prompting
**Goal:** Ask Copilot to act as a specific role (e.g., code reviewer, security expert).  
**detail**: Role-play prompting instructs Copilot to take on a particular persona or expertise, such as a security auditor or code reviewer. This can help you get more targeted feedback, uncover issues you might miss, or receive suggestions from a specific perspective.

#### ❌ Bad Prompt Examples
- "Check my code for improvement."

#### ✅ Good Prompt Examples
- "Act as a security expert. Review the Flask app for common security issues and suggest improvements."

#### Demo (on `module-5-prompting` branch)
- **Task:** Security review.
- **Prompt:**  
  *"@workspace Act as a security expert. Review the Flask app for vulnerabilities such as XSS, CSRF, insecure secrets, and OWASP 10. Suggest code changes to improve security."*

#### Reflective Questions
- How does role-play change Copilot’s output?
- What if you ask Copilot to act as a beginner?
- How would you combine role-play with other techniques?

#### Learn More
- [Role Prompting](https://platform.openai.com/docs/guides/prompt-engineering/strategies#role-prompting)
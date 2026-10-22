# Lab 5: Reflection Questions

**1. The purpose and scope of static code analysis**
*Answer:* Static analysis tools are incredibly useful because they catch hidden bugs and bad practices without even needing to run the code. They act like an automated code reviewer, pointing out things I wouldn't have noticed just by checking if the script "works."

**2. Identifying and resolving common issues**
*Answer:* This lab helped me understand why certain Python habits are dangerous. For example, using a mutable default argument (`receipts=[]`) seemed fine, but I learned it actually shares that list across every function call. I also learned why using `eval()` is a massive security risk, as it allows arbitrary code execution.

**3. Interpreting reports and applying fixes**
*Answer:* Reading the text reports from Pylint, Bandit, and Flake8 taught me how to read diagnostic warnings. By looking at the specific error codes (like Bandit's B307 or Flake8's E722) and line numbers, I could go straight to the problem and fix it based on severity, rather than guessing where the bug was.

**4. Contribution to code quality and maintainability**
*Answer:* Ultimately, these tools force you to write cleaner, safer code. Getting the Pylint score above 9.5 meant adding docstrings, fixing variable names, and managing resources properly with `with open()`. This makes the codebase much easier for another developer to read and maintain in the future.

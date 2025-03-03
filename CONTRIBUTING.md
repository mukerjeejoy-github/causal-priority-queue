# Contributing to Causal Priority Queue (CPQ)

Thank you for your interest in contributing to **Causal Priority Queue (CPQ)**! To ensure a smooth contribution process, please follow these guidelines before submitting changes.

##  Contribution Guidelines

###  How to Contribute
Since the main branch is protected, all contributions must go through a **pull request (PR)**. Follow these steps:

1. **Fork the Repository** – Click the **Fork** button on GitHub to create your own copy.
2. **Clone Your Fork** – Run the following command in your terminal:
   ```bash
   git clone https://github.com/mukerjeejoy-github/causal-priority-queue.git
   ```
3. **Create a Feature Branch** – Never work directly on `main`. Instead, create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
4. **Make Your Changes** – Implement your feature, fix, or improvement.
5. **Test Your Changes** – Ensure your code is functional and does not introduce errors.
6. **Commit & Push** – Keep your commit messages clear and descriptive:
   ```bash
   git add .
   git commit -m "Added new feature X"
   git push origin feature-branch-name
   ```
7. **Open a Pull Request (PR)** – Go to the original repository and click **"New pull request"**.
8. **Wait for Review & Approval** – Your PR will be reviewed, and you may be asked for changes before merging.

---

###  Branch Protection & Review Process
To maintain code quality, the `main` branch is protected. This means:
- **No one (including maintainers) can push directly to `main`.**
- **All changes must go through a pull request and be reviewed before merging.**
- **At least one approval is required before merging a PR.**

---

###  Reporting Issues & Feature Requests
If you found a bug or have a feature request, please:
1. **Check if an issue already exists** in the [Issues Tab](https://github.com/mukerjeejoy-github/causal-priority-queue/issues).
2. **Open a New Issue** with:
   - A clear title & description.
   - Steps to reproduce (for bugs).
   - Expected behavior vs. actual behavior.

For general discussions and feature ideas, use the [Discussions Tab](https://github.com/mukerjeejoy-github/causal-priority-queue/discussions).

---

### ** Code Standards & Style Guide**
To keep the codebase clean and maintainable, follow these standards:
- **Use meaningful variable & function names.**
- **Write clean, modular, and well-documented code.**
- **Follow Python’s PEP 8 style guide.**
- **Include docstrings for functions and classes.**
- **Ensure your code is compatible with Python 3.7+.**

---

###  Testing Your Changes
Before submitting a PR, test your changes:
- If you added a new feature, write test cases for it.
- Ensure all existing tests pass before pushing changes.
- Use `unittest` or `pytest` to validate functionality.

To run tests:
```bash
pytest tests/
```

---

###  Licensing & Contributions
By contributing to this project, you agree that your contributions will be licensed under the **MIT License**. This allows the community to freely use, modify, and distribute the code.

---

###  Contact & Support
If you have any questions, reach out via GitHub **Discussions** or open an **Issue**.

🚀 **Thank you for contributing to CPQ! Your efforts help improve this project for everyone.**


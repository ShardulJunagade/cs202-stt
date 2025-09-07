
# **Lab Assignment 1 Report**

- **Course:** CS202 – Software Tools and Techniques for CSE
- **Lab Topic:** Introduction to Version Controlling, Git Workflows, and Actions
- **Name:** Shardul Junagade
- **Roll Number:** 23110297
- **Date:** 04th August 2025

---

## **1. Introduction, Setup, and Tools (2 Marks)**

The purpose of this lab was to get familiar with **Version Control Systems (VCS)**, specifically Git, and to explore how GitHub integrates with automated workflows such as **GitHub Actions**.

By completing the lab, I aimed to:

* Understand the concepts of repository, commit, branch, and remote.
* Perform basic Git operations such as staging, committing, pushing, and pulling.
* Configure and run a GitHub Actions workflow with pylint for code quality assurance.

**Setup and Tools Used:**

* Operating System: \[Your OS, e.g., Ubuntu 22.04 / Windows 11]
* Git version: \[your git --version output]
* GitHub (remote repository hosting)
* Visual Studio Code (editor)
* Python 3.x (for pylint workflow)

*Figure 1: Git version verification*
![git version verification](./images/1.png)

---

## **2. Methodology and Execution (5 Marks)**

### **2.1 Git Configuration**

* Configured Git with `git config --global user.name` and `git config --global user.email`.
* Verified installation with `git --version`.
![git configuration](./images/3.png)

### **2.2 Initializing a Local Repository**

* Created a folder `Any_Name`.
* Initialized Git using `git init`.
![git init](./images/2.png)

### **2.3 Adding and Committing Files**

* Created `README.md` with some content.
* Staged file using `git add README.md`.
![git add](./images/4.png)
* Committed changes with `git commit -m "Initial commit"`.
* Used `git log` to view commit history.
![git commit and log](./images/5.png)


### **2.5 Remote Repository Operations**

1. **Creating a Remote Repository** – Created a new repository on GitHub.
![github repo create](./images/6.png)
2. **Connecting to GitHub** – Added remote using `git remote add origin <url>`.
3. **Pushing Changes** – Used `git push -u origin main`.
![git push](./images/7.png)

You can view changes updated on github
![github repo](./images/8.png)
4. **Cloning a Repository** – Cloned an existing repo using `git clone`.
![git clone](./images/9.png)

5. Create main.py and add a greeting message to the file on GitHub and commit it via github.
![github greeting](./images/10.png)
6. **Pulling Updates** – Used `git pull` to fetch latest changes.
![git pull](./images/11.png)


### **2.6 GitHub Actions – pylint Workflow**

* Added a Python file (`app.py`, >30 lines).
The next task was based on pylint. I created a python file with calculator code named app.py as given below:
![app.py](./images/12.png)

and committed and pushed it
![calculator push](./images/13.png)

* Created a workflow file `.github/workflows/pylint.yml`.
On github, it shows me a list of suggested workflows and I selected pylint from there.
![workflow suggestions](./images/14.png)
Then on github, I created the workflow file `.github/workflows/pylint.yml`.
![pylint workflow](./images/15.png)
* Committed the file on the main branch via github and GitHub Actions automatically ran pylint.
![pylint start](./images/16.png)
* it gave errors and tests didnt pass
![pylint errors](./images/17.png)
so i updated my calculator code to add docstrings and other fixed other errors
![update calculator](./images/18.png)
and then committed and pushed it again.
![calculator push](./images/20.png)

The pylint workflow that I had defined was automatically triggered, and it ran successfully this time and the build showed a ✅ green tick.
![pylint success](./images/21.png)
![pylint success 2](./images/22.png)



## **3. Results and Analysis (2 Marks)**

* Successfully created and managed a Git repository locally.
* Pushed and synchronized changes with GitHub.
* Demonstrated cloning and pulling operations.
* GitHub Actions successfully validated Python code with pylint, ensuring clean coding standards. the corresponding workflow was also returning the success message and the ✅ green tick was displayed
indicating success in the workflow.
![pylint success 3](./images/23.png)

Final commit history
![final commit history](./images/24.png)

*Observation:* Automated linting significantly improved the readability and maintainability of the submitted Python script.

---

## **4. Discussion and Conclusion (2 Marks)**

**Challenges Faced:**

* Initially encountered errors with `git push` due to branch mismatch (`main` vs `master`).
* Some pylint errors were difficult to interpret, but resolving them improved code quality.

**Reflections:**

* Learned how version control enables effective collaboration and backup.
* Understood the importance of CI/CD pipelines in modern software engineering.

**Conclusion:**
The lab was successful in reinforcing theoretical concepts of version control and demonstrating their application in real-world workflows. I now feel confident about managing repositories, collaborating via GitHub, and using GitHub Actions for automation.

---

## **5. References (1 Mark for Format + Style)**

* [Git Documentation](https://git-scm.com/doc)
* [GitHub Guides](https://docs.github.com/en)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* Lab Document [Shared on Google Classroom]

---

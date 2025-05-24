# 🧠 Handy Git Command Reference (with Examples)

A simple guide to common Git commands with clear explanations.

## 🔧 1. Setup

Before using Git, set your name and email (only once per machine):

```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```

## 📁 2. Start a Repository

### ➤ Create a new Git repo in your project folder

```bash
git init
```

> Think of this as telling Git: “Hey, I want to start tracking changes here!”

### ➤ Clone an existing repo (download code from GitHub)

```bash
git clone https://github.com/user/project.git
```

## 💾 3. Save Your Work (Commit Flow)

### ➤ Check what’s changed

```bash
git status
```

### ➤ Stage a file for saving

```bash
git add index.html
```

> “I want to include this file in the next save.”

### ➤ Stage everything

```bash
git add .
```

### ➤ Save your changes with a message:

```bash
git commit -m "Add homepage layout"
```

> Like hitting “Save” in your editor, but with a label explaining what you changed.

---

## 🌿 4. Work on a New Feature (Branching)

### ➤ See all branches:

```bash
git branch
```

### ➤ Create a new branch:

```bash
git branch new-feature
```

### ➤ Switch to the new branch

```bash
git checkout new-feature
```

Or both in one step:

```bash
git checkout -b new-feature
```

> "Let me work on something new without touching the main version."

---

## 🔁 5. Combine Changes (Merge)

### ➤ Go back to main branch:

```bash
git checkout main
```

### ➤ Merge changes from your feature branch

```bash
git merge new-feature
```

---

## 🌍 6. Connect to Remote (e.g., GitHub)

### ➤ Add GitHub as remote:

```bash
git remote add origin https://github.com/user/project.git
```

### ➤ Push your code online:

```bash
git push -u origin main
```

### git remote add vs. git push

| Command          | What it does                                     | When you use it                        |
| ---------------- | ------------------------------------------------ | -------------------------------------- |
| `git remote add` | Sets up the connection to a remote (like GitHub) | One time per project                   |
| `git push`       | Uploads your code to GitHub                      | Every time you want to update the repo |
----

> Upload your local work to GitHub.

### ➤ Get latest changes from remote

```bash
git pull
```

---

## 📜 7. View History

### ➤ See list of commits

```bash
git log
```

### ➤ Simple view

```bash
git log --oneline
```

### ➤ Compare changes in files

```bash
git diff
```

---

## 🧽 8. Undo Mistakes

### ➤ Undo changes in a file

```bash
git restore index.html
```

### ➤ Unstage a file

```bash
git reset HEAD index.html
```

### ➤ Revert a commit (safe undo)

```bash
git revert <commit-id>
```

---

## 💼 9. `git stash`: Temporarily Save Your Change

`git stash` is used to temporarily save your **uncommitted changes** (both staged and unstaged) without committing them. It clears your working directory so you can safely switch branches or perform other tasks, and later bring back your changes.

#### Why Use `git stash`?

Imagine you're in the middle of editing files, and suddenly need to:

- Switch branches
- Pull the latest code
- Fix a critical bug

But Git won't let you proceed because of your uncommitted changes.  
Use `git stash` to **set aside your work**, do the other task, and come back later.

#### 🧪 Example `stash` Workflow

```bash
# You're working on changes
git stash           # Save and clear working directory

git switch other-branch   # Now Git allows switching

# Do some work in another branch...

git switch original-branch
git stash pop       # Bring back your saved changes

```

### ➤ See saved stashes

```bash
git stash list
```

### ➤ Reapply stash

```bash
git stash pop
```

## 🔖 10. Tag a Version (Release)

### ➤ Add a tag

```bash
git tag v1.0
```

### ➤ Push tag to GitHub

```bash
git push origin v1.0
```

## ✨ Bonus Tips

```bash
git shortlog -sn          # List contributors
git clean -fd             # Delete untracked files
git show <commit>         # Details about a commit
```

> ✅ **Remember**: Git is like a time machine for your code. Use it often, commit small changes, and write clear messages!

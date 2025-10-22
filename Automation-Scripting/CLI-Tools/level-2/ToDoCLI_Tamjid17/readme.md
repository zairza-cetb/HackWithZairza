# Interactive Todo CLI 📝

A simple, **menu-driven command-line To-Do manager** built in Python.  
This tool allows you to **add, list, complete, delete, edit, and filter tasks** interactively, with persistent storage in JSON format. No command-line arguments are needed — just follow the prompts.

---

## ✨ Features

- 🧭 Guided, **menu-based interface** — no commands to memorize
- 📝 Add tasks interactively:
  - Task description
  - Due date (optional)
  - Priority: low / medium / high
- ✅ Mark tasks as complete
- 🗑️ Delete tasks
- ✏️ **Edit existing tasks** (description, due date, priority)
- 🔍 **Filter tasks** by:
  - Priority
  - Due date
- 📋 List all, pending, or completed tasks
- 💾 Persistent JSON storage at `~/.todo_cli.json` (default)
- 🚫 Confirmation before destructive actions

---


## 🗂 Folder Structure

    TodoCLI_Tamjid17/
    ├── main.py         # Main Python script for interactive CLI
    ├── readme.md       # Project documentation

---
## 🚀 Installation

1. Ensure **Python 3.x** is installed and added to PATH.  
2. Clone or download the repository.
3. Run these commands  
    ```
    cd TodoCLI_Tamjid17
    pip install .
    ```
4. Now type 
    ```
    todo
    ```
from your terminal and use the CLI tool
---

## 📋 Usage Guide
### Menu Overview
=== ✅ Todo CLI ===
1. Add Task
2. Edit Task
3. List All Tasks
4. List Pending Tasks
5. List Completed Tasks
6. Complete Task
7. Delete Task
8. Filter Task
9. Exit

### Add a Task

1. Select `1. Add Task`
2. Follow prompts:


---

### Edit a Task

1. Select `2. Edit Task`
2. Enter the task ID
3. You can update:
   - Description
   - Due date
   - Priority
4. Press `Enter` to keep the current value.

---

### List Tasks

- Select `3. List All Task` to list all tasks, only pending, or only completed tasks.

---

### List Pending Tasks

- Select `4. List Pending Tasks` to list all pending tasks.

---

### List Complete Tasks

- Select `5. List Complete Tasks` to list all complete tasks.

---

### Complete a Task

1. Select `6. Complete Task`
2. Enter the task ID to mark it as done.

---

### Delete a Task

1. Select `7. Delete Task`
2. Enter the task ID and confirm deletion.

---


### Filter Tasks

1. Select `8. Filter Task`
2. Select `1. By Priority` to filter based on task priority
3. Select `2. By Due Date` to filter based on a date
4. For option `1. By Priority` write high/medium/low to filter tasks
5. For option `2. By Due Date` write the date to filter tasks with due date closer to the given date

---

## 💾 Data Storage

Tasks are stored in JSON format at:
```
`~/.todo_cli.json`
```

Each task contains:

| Field         | Description                        |
|---------------|------------------------------------|
| `id`          | Auto-incremented task ID           |
| `description` | Task details                       |
| `priority`    | low / medium / high                |
| `due_date`    | Optional, YYYY-MM-DD               |
| `created_at`  | Timestamp when task was created    |
| `completed`   | True / False                       |
| `completed_at`| Timestamp when marked completed    |

---
## ⚠️ Run Tests
- In the root directory of the ToDo CLI project run this command:
```
python -m unittest discover tests
```
---
## 🧠 Technologies Used

Python Standard Library:

- `json` for storage
- `datetime` for timestamps
- `os` for file paths

---

#### Built with ❤️ by [Tamjid](https://github.com/tamjid17)
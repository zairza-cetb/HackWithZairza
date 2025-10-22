#!/usr/bin/env python3

import json
import os
from datetime import datetime

# location of the JSON file to store tasks (Home directory)
DATA_FILE = os.path.expanduser("~/.todo_cli.json")
# date format for due dates
DATE_FMT = "%Y-%m-%d"

# Load existing tasks or initialize empty list
def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save tasks to JSON file
def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

# Generate next task ID
def get_next_id(tasks):
    """Generate next task ID."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

# Display tasks in a formatted way
def print_tasks(tasks, show_completed=None):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:\n")
    print(f"{'ID':<4} {'Status':<10} {'Priority':<8} {'Due':<12} Description")
    print("-" * 60)
    for t in tasks:
        if show_completed is True and not t["completed"]:
            continue
        if show_completed is False and t["completed"]:
            continue
        status = "Done" if t["completed"] else "Pending"
        due = t["due_date"] if t["due_date"] else "-"
        print(f"{t['id']:<4} {status:<10} {t['priority']:<8} {due:<12} {t['description']}")
    print()

# Add a new task
def add_task(tasks):
    """Add a new task via user input."""
    print("\n📝 Add a New Task")
    desc = input("Enter task description: ").strip()
    if not desc:
        print("❌ Description cannot be empty.")
        return

    due_date = input("Enter due date (YYYY-MM-DD or leave blank): ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, DATE_FMT)
        except ValueError:
            print("⚠️ Invalid date format. Task not added.")
            return
    else:
        due_date = None

    priority = input("Enter priority (low/medium/high): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        print("⚠️ Invalid priority. Setting to 'medium'.")
        priority = "medium"

    new_task = {
        "id": get_next_id(tasks),
        "description": desc,
        "priority": priority,
        "due_date": due_date,
        "created_at": datetime.now().isoformat(),
        "completed": False,
        "completed_at": None,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Task added successfully!\n")

# Filter tasks by priority or due date
def filter_tasks(tasks):
    """Filter tasks by priority or due date."""
    if not tasks:
        print("\nNo tasks to filter.\n")
        return

    print("\n🔍 Filter Tasks")
    print("1. By Priority")
    print("2. By Due Date")
    choice = input("Select filter type (1/2): ").strip()

    if choice == "1":
        priority = input("Enter priority to filter (low/medium/high): ").strip().lower()
        if priority not in ["low", "medium", "high"]:
            print("❌ Invalid priority.")
            return
        filtered = [t for t in tasks if t["priority"] == priority]
        print(f"\nTasks with priority '{priority}':")
        print_tasks(filtered)

    elif choice == "2":
        due_date = input("Enter date (YYYY-MM-DD) to show tasks due on or before: ").strip()
        try:
            filter_date = datetime.strptime(due_date, DATE_FMT)
        except ValueError:
            print("❌ Invalid date format.")
            return
        filtered = [t for t in tasks if t["due_date"] and datetime.strptime(t["due_date"], DATE_FMT) <= filter_date]
        print(f"\nTasks due on or before {due_date}:")
        print_tasks(filtered)

    else:
        print("❌ Invalid choice.")

# Edit an existing task
def edit_task(tasks):
    """Edit an existing task's details."""
    print_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to edit: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    for t in tasks:
        if t["id"] == task_id:
            print("\n✏️ Editing Task:")
            print(f"Current description: {t['description']}")
            desc = input("New description (leave blank to keep): ").strip()
            if desc:
                t["description"] = desc

            print(f"Current due date: {t['due_date'] if t['due_date'] else '-'}")
            due_date = input("New due date (YYYY-MM-DD or leave blank to keep): ").strip()
            if due_date:
                try:
                    datetime.strptime(due_date, DATE_FMT)
                    t["due_date"] = due_date
                except ValueError:
                    print("⚠️ Invalid date format. Keeping old value.")

            print(f"Current priority: {t['priority']}")
            priority = input("New priority (low/medium/high or leave blank): ").strip().lower()
            if priority in ["low", "medium", "high"]:
                t["priority"] = priority
            elif priority:
                print("⚠️ Invalid priority. Keeping old value.")

            save_tasks(tasks)
            print("✅ Task updated successfully!")
            return

    print("❌ Task ID not found.")

# Mark a task as completed
def complete_task(tasks):
    """Mark a task as completed."""
    print_tasks(tasks, show_completed=False)
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("❌ Invalid input.")
        return
    for t in tasks:
        if t["id"] == task_id:
            if t["completed"]:
                print("⚠️ Task already completed.")
                return
            t["completed"] = True
            t["completed_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("✅ Task marked as completed!")
            return
    print("❌ Task ID not found.")

# Delete a task
def delete_task(tasks):
    """Delete a task."""
    print_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("❌ Invalid input.")
        return
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("❌ Task ID not found.")
        return
    confirm = input("Are you sure you want to delete this task? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Deletion canceled.")
        return
    save_tasks(new_tasks)
    print("🗑️ Task deleted successfully!")

# Main interactive loop
def main_menu():
    """Main interactive loop."""
    tasks = load_tasks()
    while True:
        print("\n=== ✅ Todo CLI ===")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. List All Tasks")
        print("4. List Pending Tasks")
        print("5. List Completed Tasks")
        print("6. Complete Task")
        print("7. Delete Task")
        print("8. Filter Task")
        print("9. Exit")

        choice = input("Choose an option (1-9): ").strip()
        if choice == "1":
            add_task(tasks)
            tasks = load_tasks()
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            print_tasks(tasks)
        elif choice == "4":
            print_tasks(tasks, show_completed=False)
        elif choice == "5":
            print_tasks(tasks, show_completed=True)
        elif choice == "6":
            complete_task(tasks)
            tasks = load_tasks()
        elif choice == "7":
            delete_task(tasks)
            tasks = load_tasks()
        elif choice == "8":
            filter_tasks(tasks)
        elif choice == "9":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()

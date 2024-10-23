class ToDoList {
  constructor() {
    this.taskList = document.querySelector("#taskList");
    this.taskInput = document.querySelector("#taskInput");
    this.addButton = document.querySelector("#addButton");

    this.addButton.addEventListener("click", () => this.addTask());
    this.taskInput.addEventListener("keypress", (event) => {
      if (event.key === "Enter") {
        this.addTask();
      }
    });
  }

  addTask() {
    const taskText = this.taskInput.value.trim();
    if (!taskText) {
      alert("Please enter a task.");
      return;
    }

    const li = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    li.appendChild(checkbox);

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-button";
    deleteButton.addEventListener("click", () => this.removeTask(li));

    li.appendChild(deleteButton);
    this.taskList.appendChild(li);
    this.taskInput.value = ""; // Clear input field
  }

  removeTask(taskItem) {
    this.taskList.removeChild(taskItem);
  }
}

// Instantiate the ToDoList class
new ToDoList();

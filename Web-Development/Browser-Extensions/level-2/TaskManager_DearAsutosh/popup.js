// Global Variables

const taskForm = document.getElementById("taskForm");
const taskTitle = document.getElementById("taskTitle");
const taskDate = document.getElementById("taskDate");
const taskList = document.getElementById("taskList");
const taskCount = document.getElementById("taskCount");
let tasks = [];

// GENERATING UNIQUE ID FROM LOCAL TIME WITH SECOND
function generateId() {
  return Date.now().toString();
}

// GET THE SELECTED PRIORITY
function getSelectedPriority() {
  const radios = document.getElementsByName("priority");
  for (let radio of radios) {
    if (radio.checked) return radio.value;
  }
  return "Low"; // Default
}

// RENDERING ALL TASKS
function renderTasks() {
  taskList.innerHTML = "";

  // SORT BY PRIORITY (HIGH > MEDIUM > LOW)
  const priorityOrder = { High: 3, Medium: 2, Low: 1 };
  const sortedTasks = [...tasks].sort((a, b) => {
    return priorityOrder[b.priority] - priorityOrder[a.priority];
  });

  sortedTasks.forEach((task) => {
    const li = document.createElement("li");

    const taskHeader = document.createElement("div");
    taskHeader.className = "task-header";

    const titleSpan = document.createElement("span");
    titleSpan.textContent = task.title;
    titleSpan.className = "task-title";

    if (task.completed) {
      titleSpan.style.textDecoration = "line-through";
      titleSpan.style.color = "#999";
    }

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.addEventListener("change", () => toggleTaskComplete(task.id));

    taskHeader.appendChild(checkbox);
    taskHeader.appendChild(titleSpan);

    const meta = document.createElement("div");
    meta.className = "task-meta";
    meta.textContent = `📅 ${task.dueDate} | ⚡ ${task.priority}`;

    const actions = document.createElement("div");
    actions.className = "task-actions";

    const editBtn = document.createElement("button");
    editBtn.innerHTML = `<i class="fa-solid fa-pen"></i>`;
    editBtn.title = "Edit Task";
    editBtn.addEventListener("click", () => editTask(task.id));

    const deleteBtn = document.createElement("button");
    deleteBtn.innerHTML = `<i class="fa-solid fa-trash"></i>`;
    deleteBtn.title = "Delete Task";
    deleteBtn.addEventListener("click", () => deleteTask(task.id));

    actions.appendChild(editBtn);
    actions.appendChild(deleteBtn);

    li.appendChild(taskHeader);
    li.appendChild(meta);
    li.appendChild(actions);

    taskList.appendChild(li);
  });

  // UPDATE TASK COUNT
  const pending = tasks.filter((t) => !t.completed).length;
  taskCount.textContent = `${pending} pending task${pending !== 1 ? "s" : ""}`;
}

// ================CRUD Operations================

// ADD A NEW TASK
taskForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = taskTitle.value.trim();
  const dueDate = taskDate.value;
  const priority = getSelectedPriority();

  if (!title || !dueDate) return;

  const newTask = {
    id: generateId(),
    title,
    dueDate,
    priority,
    completed: false,
  };

  tasks.push(newTask);
  await saveTasks();

  taskTitle.value = "";
  taskDate.value = "";
  renderTasks();
});

// TOGGLE COMPLETION OF A TASK
function toggleTaskComplete(id) {
  const task = tasks.find((t) => t.id === id);
  if (task) {
    task.completed = !task.completed;
    saveTasks();
    renderTasks();
  }
}

// EDIT A TASK
function editTask(id) {
  const task = tasks.find((t) => t.id === id);
  if (!task) return;

  const newTitle = prompt("Edit Task Title:", task.title);
  if (newTitle !== null && newTitle.trim() !== "") {
    task.title = newTitle.trim();
  }

  const newDate = prompt("Edit Due Date (YYYY-MM-DD):", task.dueDate);
  if (newDate) {
    task.dueDate = newDate;
  }

  saveTasks();
  renderTasks();
}

// DELETE A TASK
function deleteTask(id) {
  if (confirm("Are you sure you want to delete this task?")) {
    tasks = tasks.filter((t) => t.id !== id);
    saveTasks();
    renderTasks();
  }
}

// SYNC WITH CHROME STORAGE
async function saveTasks() {
  await chrome.storage.sync.set({ tasks });
}

async function loadTasks() {
  const result = await chrome.storage.sync.get("tasks");
  tasks = result.tasks || [];
  renderTasks();
}

// INITIALIZE
document.addEventListener("DOMContentLoaded", loadTasks);







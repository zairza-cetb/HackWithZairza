const TaskArray = [];
const addTask = () => {
  const task = document.querySelector(".container");
  const taskval = task.value.trim();
  if (taskval) {
    TaskArray.push(taskval);
    task.value = "";
    const taskList = document.querySelector(".tasks");
    taskList.innerHTML = "";
    TaskArray.forEach((task, index) => {
      taskList.innerHTML += `<div class="task">
        <input type="checkbox" />
        <p>${task}</p>
        <button class="delete"  onclick="deleteTask()">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>`;
    });
  } else {
    alert("Please enter a task");
  }
};
const deleteTask = (index) => {
  TaskArray.splice(index, 1);
  const taskList = document.querySelector(".tasks");
  taskList.innerHTML = "";
  TaskArray.forEach((task, index) => {
    taskList.innerHTML += `<div class="task">
        <input type="checkbox" />
        <p>${task}</p>
        <button class="delete"  >
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>`;
  });
};

const date = document.querySelector("h2");
const today = new Date();
date.innerHTML = today.toDateString();

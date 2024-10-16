// Initialize an empty array to store tasks
const TaskArray = [];

// Function to add a new task
const addTask = () => {
  // Get the input field and its value
  const task = document.querySelector(".container");
  const taskval = task.value.trim();

  // Check if the input value is not empty
  if (taskval) {
    // Add the task to the TaskArray
    TaskArray.push(taskval);
    // Clear the input field
    task.value = "";

    // Get the task list container
    const taskList = document.querySelector(".tasks");
    // Clear the current task list
    taskList.innerHTML = "";

    // Iterate over the TaskArray and update the task list
    TaskArray.forEach((task, index) => {
      taskList.innerHTML += `<div class="task">
        <input type="checkbox" />
        <p>${task}</p>
        <button class="delete" onclick="deleteTask(${index})">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>`;
    });
  } else {
    // Alert the user if the input field is empty
    alert("Please enter a task");
  }
};

// Function to delete a task
const deleteTask = (index) => {
  // Remove the task from the TaskArray at the specified index
  TaskArray.splice(index, 1);

  // Get the task list container
  const taskList = document.querySelector(".tasks");
  // Clear the current task list
  taskList.innerHTML = "";

  // Iterate over the TaskArray and update the task list
  TaskArray.forEach((task, index) => {
    taskList.innerHTML += `<div class="task">
        <input type="checkbox" />
        <p>${task}</p>
        <button class="delete" onclick="deleteTask(${index})">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>`;
  });
};

// Get the h2 element to display the current date
const date = document.querySelector("h2");
// Get the current date
const today = new Date();
// Set the inner HTML of the h2 element to the current date
date.innerHTML = today.toDateString();

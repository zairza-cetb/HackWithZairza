const taskInput = document.getElementById('new-task');
const taskList = document.getElementById('task-list');
const addTaskButton = document.getElementById('add-task-btn');

// Function to add a new task to the list
function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === "") return; 

    const listItem = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    const label = document.createElement('label');
    label.textContent = taskText;

    // Create a remove button for the task
    const removeButton = document.createElement('button');
    removeButton.textContent = 'X';
    removeButton.classList.add('remove-task-btn');

    removeButton.addEventListener('click', function() {
        listItem.remove();
    });

    listItem.appendChild(checkbox);
    listItem.appendChild(label);
    listItem.appendChild(removeButton);
    // Append the list item to the task list
    taskList.appendChild(listItem);

    taskInput.value = "";
}

addTaskButton.addEventListener('click', addTask);
//enter key
taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});
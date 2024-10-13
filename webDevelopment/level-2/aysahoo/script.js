const taskInput = document.getElementById('new-task');
const taskList = document.getElementById('task-list');
const addTaskButton = document.getElementById('add-task-btn');


function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === "") return; 

    const listItem = document.createElement('li');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const label = document.createElement('label');
    label.textContent = taskText;

    const removeButton = document.createElement('button');
    removeButton.textContent = 'X';
    removeButton.classList.add('remove-task-btn');

    removeButton.addEventListener('click', function() {
        listItem.remove();
    });

    listItem.appendChild(checkbox);
    listItem.appendChild(label);
    listItem.appendChild(removeButton);
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
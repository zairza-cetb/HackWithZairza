// --- Authentication Logic ---

document.getElementById('show-register')?.addEventListener('click', function() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
});

document.getElementById('show-login')?.addEventListener('click', function() {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
});

// Register a new user with role selection
document.getElementById('register-btn')?.addEventListener('click', function() {
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;
    const role = document.getElementById('register-role').value; // Get the selected role

    if (username && password) {
        localStorage.setItem(username, JSON.stringify({ password: password, role: role, tasks: [] }));
        alert('Registration successful! Please login.');
        document.getElementById('register-username').value = "";
        document.getElementById('register-password').value = "";
        document.getElementById('register-form').style.display = 'none';
        document.getElementById('login-form').style.display = 'block';
    } else {
        alert('Please fill in all fields.');
    }
});

// Log in a registered user
document.getElementById('login-btn')?.addEventListener('click', function() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    const userData = JSON.parse(localStorage.getItem(username));
    if (userData && userData.password === password) {
        sessionStorage.setItem('loggedInUser', username);
        window.location.href = 'todo.html';
    } else {
        alert('Invalid login credentials.');
    }
});

// --- To-Do List Logic ---

if (window.location.pathname.endsWith('todo.html')) {
    if (!sessionStorage.getItem('loggedInUser')) {
        window.location.href = 'index.html';
    }

    const username = sessionStorage.getItem('loggedInUser');
    const userData = JSON.parse(localStorage.getItem(username));
    const taskInput = document.getElementById('new-task');
    const taskList = document.getElementById('task-list');
    const addTaskButton = document.getElementById('add-task-btn');
    const welcomeMessage = document.getElementById('welcome-message');

    welcomeMessage.textContent = `Welcome, ${username} (${userData.role})!`;

    // Define Permissions
    const permissions = {
        'User': {
            canAddTask: true,
            canDeleteOwnTask: true,
            canDeleteOthersTask: false
        },
        'Admin': {
            canAddTask: true,
            canDeleteOwnTask: true,
            canDeleteOthersTask: true
        }
    };

    // Function to load tasks
    function loadTasks() {
        taskList.innerHTML = ''; // Clear previous tasks

        for (const [taskOwner, taskData] of Object.entries(localStorage)) {
            const taskOwnerData = JSON.parse(taskData);
            if (taskOwnerData.tasks) {
                taskOwnerData.tasks.forEach((task, index) => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${task.text} (Created by: ${taskOwner})`;

                    if (task.completed) {
                        listItem.style.textDecoration = "line-through";
                    }

                    // Checkbox to mark task as completed
                    const checkbox = document.createElement('input');
                    checkbox.type = "checkbox";
                    checkbox.checked = task.completed;
                    checkbox.addEventListener('change', function() {
                        task.completed = checkbox.checked;
                        updateUserData(taskOwnerData, taskOwner);
                        loadTasks(); // Reload tasks to apply the line-through effect
                    });

                    // Add a remove button for each task
                    const removeBtn = document.createElement('button');
                    removeBtn.textContent = 'Remove';

                    // Restrict remove task based on role permissions
                    if ((permissions[userData.role].canDeleteOwnTask && taskOwner === username) || 
                        (permissions[userData.role].canDeleteOthersTask && taskOwner !== username)) {
                        removeBtn.addEventListener('click', function() {
                            taskOwnerData.tasks.splice(index, 1);
                            updateUserData(taskOwnerData, taskOwner);
                            loadTasks(); // Reload tasks after removing
                        });
                    } else {
                        removeBtn.disabled = true; // Disable remove button for unauthorized users
                        removeBtn.title = "You don't have permission to delete this task.";
                    }

                    listItem.appendChild(checkbox);
                    listItem.appendChild(removeBtn);
                    taskList.appendChild(listItem);
                });
            }
        }
    }

    // Add new task functionality
    addTaskButton.addEventListener('click', function() {
        const taskText = taskInput.value.trim();

        if (permissions[userData.role].canAddTask) {
            if (taskText !== "") {
                userData.tasks.push({ text: taskText, completed: false });
                updateUserData(userData, username);
                taskInput.value = "";
                loadTasks();
            }
        } else {
            alert('You do not have permission to add a task.');
        }
    });

    // Function to update user data in localStorage
    function updateUserData(data, username) {
        localStorage.setItem(username, JSON.stringify(data));
    }

    // Load tasks when the page loads
    loadTasks();

    // Logout functionality
    document.getElementById('logout-btn').addEventListener('click', function() {
        sessionStorage.removeItem('loggedInUser');
        window.location.href = 'index.html';
    });

    // Auto-logout after 5 minutes
    setTimeout(() => {
        sessionStorage.removeItem('loggedInUser');
        alert('Session expired. Logging out.');
        window.location.href = 'index.html';
    }, 300000); // 5 minutes
}
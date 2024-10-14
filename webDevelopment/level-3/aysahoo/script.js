//Auth Logic

// Switch between Login and Register forms
document.getElementById('show-register')?.addEventListener('click', function() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
});

document.getElementById('show-login')?.addEventListener('click', function() {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
});

// Register a new user
document.getElementById('register-btn')?.addEventListener('click', function() {
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;

    if (username && password) {
        localStorage.setItem(username, JSON.stringify({ password: password, tasks: [] }));
        alert('Registration successful! Please login.');
        document.getElementById('register-username').value = "";
        document.getElementById('register-password').value = "";
        document.getElementById('register-form').style.display = 'none';
        document.getElementById('login-form').style.display = 'block';
    } else {
        alert('Please fill in both fields.');
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

//To-Do List Logic

if (window.location.pathname.endsWith('todo.html')) {
    // Redirect to login if user is not logged in
    if (!sessionStorage.getItem('loggedInUser')) {
        window.location.href = 'index.html';
    }

    const username = sessionStorage.getItem('loggedInUser');
    const userData = JSON.parse(localStorage.getItem(username));
    const taskInput = document.getElementById('new-task');
    const taskList = document.getElementById('task-list');
    const addTaskButton = document.getElementById('add-task-btn');
    const welcomeMessage = document.getElementById('welcome-message');

    welcomeMessage.textContent = `Welcome, ${username}!`;

    // Load the user's tasks from localStorage
    function loadTasks() {
        taskList.innerHTML = ''; 

        userData.tasks.forEach((task, index) => {
            const listItem = document.createElement('li');
            listItem.classList.add('task-item');

            if (task.completed) {
                listItem.style.textDecoration = "line-through";
            }

            // Checkbox
            const checkbox = document.createElement('input');
            checkbox.type = "checkbox";
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', function() {
                task.completed = checkbox.checked;
                updateUserData();
                loadTasks();
            });

            //remove button
            const removeBtn = document.createElement('button');
            removeBtn.textContent = 'X';
            removeBtn.classList.add('remove-task-btn');
            removeBtn.addEventListener('click', function() {
                userData.tasks.splice(index, 1);
                updateUserData();
                loadTasks();
            });

            listItem.appendChild(checkbox);
            const taskText = document.createTextNode(task.text);
            listItem.appendChild(taskText);
            listItem.appendChild(removeBtn);
            taskList.appendChild(listItem);
        });
    }

    // Add new task
    addTaskButton.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText !== "") {
            userData.tasks.push({ text: taskText, completed: false });
            updateUserData();
            taskInput.value = "";
            loadTasks();
        }
    });

    // Update
    function updateUserData() {
        localStorage.setItem(username, JSON.stringify(userData));
    }

    // Load tasks when the page loads
    loadTasks();

    // Logout
    document.getElementById('logout-btn').addEventListener('click', function() {
        sessionStorage.removeItem('loggedInUser');
        window.location.href = 'index.html';
    });

    // Auto-logout after 5 minutes (300000 milliseconds)
    setTimeout(() => {
        sessionStorage.removeItem('loggedInUser');
        alert('Session expired. Logging out.');
        window.location.href = 'index.html';
    }, 300000);
}
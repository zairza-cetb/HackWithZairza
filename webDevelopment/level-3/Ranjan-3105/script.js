// ======= AUTHENTICATION CODE =======
document.querySelector("#show-register")?.addEventListener("click", (e) => {
  e.preventDefault(); // Prevent default action
  document.querySelector(".login").style.display = "none";
  document.querySelector(".register").style.display = "flex";
});

document.querySelector("#show-login")?.addEventListener("click", (e) => {
  e.preventDefault(); // Prevent default action
  document.querySelector(".register").style.display = "none";
  document.querySelector(".login").style.display = "flex";
});

// Register new user
document.querySelector("#register-button").addEventListener("click", (e) => {
  e.preventDefault(); // Prevent default button action
  const username = document.getElementById("register-username").value.trim();
  const password = document.getElementById("register-password").value.trim();

  if (username && password) {
    let users = JSON.parse(localStorage.getItem("users") || "[]");

    // Check if username already exists
    if (users.find((user) => user.username === username)) {
      alert("Username already exists. Try a different one.");
      return;
    }

    // Add new user
    users.push({ username, password });
    localStorage.setItem("users", JSON.stringify(users));
    alert("Registration successful! You can now log in.");
    document.querySelector(".register").style.display = "none";
    document.querySelector(".login").style.display = "flex";
  } else {
    alert("Please enter both username and password.");
  }
});

// User login
document.querySelector("#login-btn").addEventListener("click", (e) => {
  e.preventDefault(); // Prevent default button action
  const username = document.getElementById("login-username").value.trim();
  const password = document.getElementById("login-password").value.trim();

  if (username && password) {
    let users = JSON.parse(localStorage.getItem("users") || "[]");

    // Authenticate user
    const user = users.find(
      (user) => user.username === username && user.password === password
    );
    if (user) {
      alert("Login successful!");
      localStorage.setItem("currentUser", username); // Set logged-in user
      document.querySelector(".auth-container").style.display = "none";
      document.querySelector(".todo-app").style.display = "block"; // Show to-do app
      loadUserTodos(); // Load the user's specific to-do list
      countdown( "ten-countdown", 10, 0 ); //countdowwn startsss   

      //auto-logout after 10 mins => 600s => 6,00,000ms
      setTimeout(() => {
        alert("Session expired. Logging out.");
        logOut();
        
      }, 600000);

    } else {
      alert("Invalid username or password.");
    }
  } else {
    alert("Please enter both username and password.");
  }
});

// ======= TODO LIST CODE =======
const todoForm = document.querySelector(".todo-form");
const todoInput = document.getElementById("todo-input");
const todoListUL = document.getElementById("todo-list");
let allTasks = []; // Will hold the current user's to-dos

// Prevent form submission from refreshing the page
todoForm.addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent the form from submitting and refreshing the page
  addTodo(); // Call the function to add a new to-do
});

// Function to add a new to-do
function addTodo() {
  const todoText = todoInput.value.trim();
  if (todoText.length > 0) {
    const todoObject = { text: todoText, completed: false };
    allTasks.push(todoObject);
    updateTodoList();
    saveTodos();
    todoInput.value = "";
  } else {
    alert("OOPS! You forgot to enter the task.");
  }
}

// Render the to-do list for the logged-in user
function updateTodoList() {
  todoListUL.innerHTML = "";
  allTasks.forEach((todo, todoIndex) => {
    todoItem = createTodoItem(todo, todoIndex);
    todoListUL.append(todoItem);
  });
}

// Create a new to-do item element
function createTodoItem(todo, todoIndex) {
  const todoId = "todo-" + todoIndex;
  const todoLI = document.createElement("li");
  todoLI.className = "todo";
  todoLI.innerHTML = `
        <input type="checkbox" id="${todoId}">
        <label class="custom-checkbox" for="${todoId}">
            <svg fill="transparent" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/></svg>
        </label>
        <label for="${todoId}" class="todo-text">
            ${todo.text}
        </label>
        <button class="delete-button">
            <svg fill="var(--secondary-color)" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z"/></svg>
        </button>
    `;

  // Delete button
  todoLI.querySelector(".delete-button").addEventListener("click", (e) => {
    e.preventDefault(); // Prevent default button action
    deleteTodoItem(todoIndex);
  });

  // Completed checkbox
  const checkbox = todoLI.querySelector("input");
  checkbox.addEventListener("change", () => {
    allTasks[todoIndex].completed = checkbox.checked;
    saveTodos();
  });

  checkbox.checked = todo.completed;
  return todoLI;
}

// Delete a to-do item
function deleteTodoItem(todoIndex) {
  allTasks = allTasks.filter((_, i) => i !== todoIndex);
  saveTodos();
  updateTodoList();
}

// Save the user's to-do list in localStorage
function saveTodos() {
  const currentUser = localStorage.getItem("currentUser");
  localStorage.setItem(`${currentUser}-todos`, JSON.stringify(allTasks));
}

// Load the to-do list of the logged-in user
function loadUserTodos() {
  const currentUser = localStorage.getItem("currentUser");
  const todos = localStorage.getItem(`${currentUser}-todos`) || "[]";
  allTasks = JSON.parse(todos);
  updateTodoList();
}

//logout function
const logoutbtn = document.getElementById("logout-btn");

logoutbtn.addEventListener("click", () => {
  logOut();
  alert("you have been successfully logged out !");
});

function logOut() {
  location.reload();
}


//countdown timer
function countdown( elementName, minutes, seconds )
{
    var element, endTime, hours, mins, msLeft, time;

    function twoDigits( n )
    {
        return (n <= 9 ? "0" + n : n);
    }

    function updateTimer()
    {
        msLeft = endTime - (+new Date);
        if ( msLeft < 1000 ) {
            element.innerHTML = "Time is up!";
        } else {
            time = new Date( msLeft );
            hours = time.getUTCHours();
            mins = time.getUTCMinutes();
            element.innerHTML = "Time Left => " + (hours ? hours + ':' + twoDigits( mins ) : mins) + ':' + twoDigits( time.getUTCSeconds() );
            setTimeout( updateTimer, time.getUTCMilliseconds() + 500 );
        }
    }

    element = document.getElementById( elementName );
    endTime = (+new Date) + 1000 * (60*minutes + seconds) + 500;
    updateTimer();
}


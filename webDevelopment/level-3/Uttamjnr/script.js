const task = document.getElementById("new-task");
const atb = document.getElementById("atb");
const taskList = document.querySelector("ul");

// Authentication Elements
const authContainer = document.getElementById("auth-container");
const todoContainer = document.getElementById("todo-container");
const authButton = document.getElementById("auth-button");
const toggleAuth = document.getElementById("toggle-auth");
const authTitle = document.getElementById("auth-title");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const switchAuthText = document.getElementById("switch-auth");
const logoutButton = document.getElementById("logout-button");

let users = JSON.parse(localStorage.getItem("users")) || {}; // Store users
let currentUser = null;
let isRegistering = false;
let autoLogoutTimer;

// Add task functionality
let addTask = () => {
  let num = Math.random();
  let taskText = task.value.trim();
  const li = document.createElement("li");
  if (taskText != "") {
    li.innerHTML = `<input type="checkbox" id="${num}" />
        <label for="${num}">${taskText} </label>`;
    
    const removeButton = document.createElement("img");
    removeButton.src = "elements/xmark-solid.svg";
    removeButton.classList.add("remove-btn");
    li.appendChild(removeButton);
    taskList.append(li);

    removeButton.addEventListener("click", () => {
      li.remove();
    });
  }
};

atb.addEventListener("click", () => {
  addTask();
  task.value = "";
});

task.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    addTask();
    task.value = "";
  }
});

// Toggle between login and registration
toggleAuth.addEventListener("click", () => {
  isRegistering = !isRegistering;
  if (isRegistering) {
    authTitle.innerText = "Register";
    authButton.innerText = "Register";
    switchAuthText.innerHTML = "Already have an account? <span id='toggle-auth'>Login</span>";
  } else {
    authTitle.innerText = "Login";
    authButton.innerText = "Login";
    switchAuthText.innerHTML = "Don't have an account? <span id='toggle-auth'>Register</span>";
  }
});

// Handle login or registration
authButton.addEventListener("click", () => {
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  if (username === "" || password === "") {
    alert("Please enter both username and password.");
    return;
  }

  if (isRegistering) {
    if (users[username]) {
      alert("User already exists.");
    } else {
      users[username] = { password };
      localStorage.setItem("users", JSON.stringify(users));
      alert("Registration successful! Please login.");
      authContainer.style.display = "none";
      todoContainer.style.display = "block";
    }
  } else {
    if (users[username] && users[username].password === password) {
      alert("Login successful!");
      currentUser = username;
      startSession();
    } else {
      alert("Invalid username or password.");
    }
  }
});

// Start user session and display the to-do list
function startSession() {
  authContainer.style.display = "none";
  todoContainer.style.display = "block";
  resetAutoLogout();
}

// Logout the user and end the session
function logout() {
  currentUser = null;
  authContainer.style.display = "block";
  todoContainer.style.display = "none";
  clearTimeout(autoLogoutTimer);
  alert("You have been logged out.");
}

// Handle logout button click
logoutButton.addEventListener("click", logout);

// Auto logout after 5 minutes of inactivity
function resetAutoLogout() {
  clearTimeout(autoLogoutTimer);
  autoLogoutTimer = setTimeout(logout, 300000); // 5 minutes
}


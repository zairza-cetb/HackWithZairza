const inputBox = document.getElementById("input_task");
const listContainer = document.getElementById("task_container");

// function to save the data even after reload
function saveData() {
    localStorage.setItem("data", listContainer.innerHTML); // the innerHTML of listContiner is saved in the key "data"
}

// function to add new tasks
function addtask() {
    if (inputBox.value === '') {
        alert("You must write something!"); // prevents adding blank tasks
    } else {
        let li = document.createElement("li"); // creates new li elements containing tasks
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
        saveData();
    }
    inputBox.value = ""; // after adding the tasks, the input is cleared
}

// to add new tasks after pressing Enter button on the keyboard
window.addEventListener(
    "keydown", // on pressing the key
  (event) => {
    switch (event.key) {
        case "Enter":
            event.preventDefault(); // prevents any default action of pressing enter
            addtask(); // calls the addtask function
        default:
            return; // in case any other button is pressed
    }
},
true,
);      

// function to check or uncheck the task on pressing on it
listContainer.addEventListener("click", function(e){
    if (e.target.tagName === "LI"){
        e.target.classList.toggle("checked"); // adds or removes a class checked
        saveData();
    } 
    else if (e.target.tagName === "SPAN"){
        e.target.parentElement.remove(); // if x is pressed, it removes the corresponding task
        saveData();
    }
}, false);

// function to show the added tasks even after reloads
function showTask() {
    listContainer.innerHTML = localStorage.getItem("data"); // gets the saved innerHTML from "data"
}

// calling the function show the added tasks and their updates
showTask();


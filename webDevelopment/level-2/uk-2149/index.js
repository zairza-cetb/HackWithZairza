const inputBox = document.getElementById("input_task");
const listContainer = document.getElementById("task_container");

function saveData() {
    localStorage.setItem("data", listContainer.innerHTML);
}

function addtask() {
    if (inputBox.value === '') {
        alert("You must write something!");
    } else {
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
        saveData();
    }
    inputBox.value = "";
}

window.addEventListener(
    "keydown",
  (event) => {
    switch (event.key) {
        case "Enter":
            event.preventDefault();
            addtask();
        default:
            return;
    }
},
true,
);      

listContainer.addEventListener("click", function(e){
    if (e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    } 
    else if (e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function showTask() {
    listContainer.innerHTML = localStorage.getItem("data");
}

showTask();


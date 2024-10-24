const task = document.getElementById("new-task");
const atb = document.getElementById("atb");
const taskList = document.querySelector("ul");
// function for adding task

let addTask = () => {
  //for unique id
  let num = Math.random();
  let taskText = task.value.trim();
  const li = document.createElement("li");
  if (taskText != "") {
    li.innerHTML = `<input type="checkbox" id="${num}" />
        <label for="${num}">${taskText} </label>
        `;

    //creating remove button
    const removeButton = document.createElement("img");
    removeButton.src = "elements/xmark-solid.svg";
    removeButton.classList.add("remove-btn");
    //append to html
    li.appendChild(removeButton);
    taskList.append(li);
    //event listener for removebutton
    removeButton.addEventListener("click", () => {
      li.remove();
    });
  }
};
// for add button(atb- addTaskButton)
atb.addEventListener("click", () => {
  addTask();
  task.value = "";
});
//for Enter Keypress
task.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    addTask();
    task.value = "";
  }
});

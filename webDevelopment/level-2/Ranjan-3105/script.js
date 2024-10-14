const todoForm = document.querySelector('form');
const todoInput = document.getElementById('todo-input');
const todoListUL = document.getElementById('todo-list');

// allTasks is the object stored in localstorage. get storage is used to fetch the data from the localstorage, also calling the update function.
let allTasks = getTodos();
updateTodoList();

todoForm.addEventListener('submit', function(e){
    e.preventDefault();
    addTodo();
})

// function to add todo to alltodo array.
function addTodo(){
    //trimmed to avoid unnecessary space
    const todoText = todoInput.value.trim();
    if(todoText.length > 0){
        const todoObject = {
            text: todoText,
            completed: false
        }
        allTasks.push(todoObject);
        updateTodoList();
        //saving to localStorage each time when new task added.
        saveTodos();
        todoInput.value = "";
    }else{
        //edgecase, when user input is null.
        alert("OOPS! You forgot to enter the task .")
    } 
}

//update and render all todos from the array passed as an array in the addTodo fn above.
function updateTodoList(){
    todoListUL.innerHTML = "";
    allTasks.forEach((todo, todoIndex)=>{
        todoItem = createTodoItem(todo, todoIndex);
        todoListUL.append(todoItem);
    })
}

//createTodoItem creates template for rendering the the task.
function createTodoItem(todo, todoIndex){
    const todoId = "todo-"+todoIndex;
    const todoLI = document.createElement("li");
    const todoText = todo.text;
    todoLI.className = "todo";
    todoLI.innerHTML = `
        <input type="checkbox" id="${todoId}">
        <label class="custom-checkbox" for="${todoId}">
            <svg fill="transparent" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z"/></svg>
        </label>
        <label for="${todoId}" class="todo-text">
            ${todoText}
        </label>
        <button class="delete-button">
            <svg fill="var(--secondary-color)" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z"/></svg>
        </button>
    `
    //delete button
    const deleteButton = todoLI.querySelector(".delete-button");
    deleteButton.addEventListener("click", ()=>{
        deleteTodoItem(todoIndex);
    })

    //completed check doer
    const checkbox = todoLI.querySelector("input");
    checkbox.addEventListener("change", ()=>{
        allTasks[todoIndex].completed = checkbox.checked;
        saveTodos();
    })
    //to render the checked box when reloaded
    checkbox.checked = todo.completed;
    return todoLI;
}

//delete task function
function deleteTodoItem(todoIndex){
    allTasks = allTasks.filter((_, i)=> i !== todoIndex);
    saveTodos();
    updateTodoList();
}

//localStorage so that reloading doesn't affect the progress.
function saveTodos(){
    const todosJson = JSON.stringify(allTasks);
    localStorage.setItem("todos", todosJson);
}

//getting the data of todos stored in localStorage.
function getTodos(){
    const todos = localStorage.getItem("todos") || "[]";
    return JSON.parse(todos);
}

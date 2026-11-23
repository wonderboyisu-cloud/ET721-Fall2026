// load all tasks
function loadTasks() {
    fetch("/get_tasks")
        .then(response => response.json())
        .then(tasks => {
            const list = document.getElementById("taskList");
            list.innerHTML = "";
            tasks.forEach(t => createTaskElement(t.id, t.task));
        })
        .catch(error => console.error("Error loading tasks:", error));
}

// load all tasks when page loads
window.onload = loadTasks;

function addTask() {
    const input = document.getElementById("taskInput");
    const task = input.value.trim();

    if (task === "") return;

    fetch("/add_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: task })
    })
    .then(() => {
        input.value = "";
        loadTasks();
    })
    .catch(error => console.error("Error adding task:", error));
}

function createTaskElement(id, taskText) {
    const list = document.getElementById("taskList");
    const li = document.createElement("li");
    li.textContent = taskText + " ";
    li.classList.add("task-item");

    const btn = document.createElement("button");
    btn.innerHTML = "&#10060;";
    btn.onclick = () => deleteTask(id);
    btn.classList.add("btn-delete-item");

    li.appendChild(btn);
    list.appendChild(li);
}

function deleteTask(id) {
    fetch("/delete_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: id })
    })
    .then(() => loadTasks())
    .catch(error => console.error("Error deleting task:", error));
}





















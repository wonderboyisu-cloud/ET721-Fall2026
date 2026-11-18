// load all tasks
function loadTasks(){
    fetch("/get_tasks")
    .then(response => response.json())
    .then(tasks => {
        const list = document.querySelector('#tasklist')
        list.innerHTML = "";

        tasks.forEach(task => {
            const li = document.createElement('li')
            li.textContent = task.task;
            li.classList.add("task_item");
            list.appendChild(li);

            // create a delete button for each task
            const btn = document.createElement("button")
            btn.innerHTML = "&#10060" // unicode for cross mark
            btn.classList.add("btndeletetask")
            btn.onclick = () => {
                fetch("/delete_task", {
                    method: "POST",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify({task: task.task})

                })
                .then(() => loadTasks());
            };
            li.appendChild(btn);

        });

    });

}

// load all tasks when page loads
window.onload = loadTasks;

function addtask(){
    const inputtask = document.querySelector("#taskinput")
    const task = inputtask.value.trim()

    if (task === "") return;
    
    fetch("/add_task", {
        method: "POST",
        headers: {"Content-Type":"applicatiob/json"},
        body: JSON.stringify({task:task})

    })
    .then(()=>{
        inputtask.value = ""
        loadTasks()
        
    })
}










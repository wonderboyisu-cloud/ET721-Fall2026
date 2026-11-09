console.log("Isaam Shah")

// collect items from the form
const itemForm = document.querySelector('#itemForm')

// add an event to the form
itemForm.addEventListener("submit", async function(event) {
    event.preventDefault()
    const name = document.querySelector('#name').value
    const price = document.querySelector('#price').value

    try {
        // await to pause  request until the request is finished
        // fetch() sends an HTTP request to server
        const res = await fetch("http://127.0.0.1:5000/items", {method: 'POST', headers: {"Content-type":"application/json"},
            body: JSON.stringify({name: name, price: Number(price)})
            } 
            
        )
        const data = await res.json()
        document.querySelector('#response').innerText = "Response: " + JSON.stringify(data)
    } 
    
    catch(error){
        document.querySelector('#response').innerText = "ERROR: " + error
    }
    
})

// LOADING ITEMS
async function loaditems() {
    const res = await fetch("http://127.0.0.1:5000/items")
    const data = await res.json()

    // collect the element to print all items
    const list = document.querySelector("#itemslist")
    list.innerHTML = ""

    // use a loop to place each item in the json data to a list
    for (const id in data) {
        const item = data[id]
        const li = document.createElement("li")
        li.innerHTML = `
        ID = ${id} | Name = ${item.name} | Price = ${item.price}
        <button onclick = "showupdateform('${id}', '${item.name}', '${item.price}')"> Update </button>
        <button onclick = "deleteitem('${id}')"> Delete </button>
        `
        list.appendChild(li)
    }

}

// function to collect selected item
function showupdateform(id, name, price) {
    document.querySelector('#updatesection').style.display = "block"
    document.querySelector('#updateName').value = name
    document.querySelector('#updateID').value = id
    document.querySelector('#updatePrice').value = price
}

// function to update the selected item name or price
async function updateitem() {
    const id = document.querySelector('#updateID').value
    const name = document.querySelector('#updateName').value
    const price = document.querySelector('#updatePrice').value

    // update the json data in localhost
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, {
        method: "PUT",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify({name: name, price: Number(price)})

    })
    const html = await res.text()
    document.body.innerHTML = html

}

// DELETE ITEM
async function deleteitem(id) {
    const res = await fetch(`http://127.0.0.1:5000/items/${id}`, 
    {
        method: "DELETE"
    })
    
}








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














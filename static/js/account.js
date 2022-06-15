// DOM Manipulation
function remove_element_by_request_id(req_id) {
    let input_element = document.querySelector(`input[value="${req_id}"]`)
    let request_delete_div = input_element.parentElement
    request_delete_div.remove()
    if (!check_for_empty()) {
        create_empty_condition()
    }
}

function create_request_id_element(item){
    let req_id_element = document.createElement("input")
    req_id_element.setAttribute("type", "hidden")
    req_id_element.setAttribute("name", "req_id")
    req_id_element.setAttribute("value", `${item.req_id}`)

    return req_id_element
}

function create_user_id_element(item) {
    let user_id_element = document.createElement("input")
    user_id_element.setAttribute("type", "hidden")
    user_id_element.setAttribute("name", "user_id")
    user_id_element.setAttribute("class", "user-id-request")
    user_id_element.setAttribute("value", `${item.user_id}`)

    return user_id_element
}

function create_request_amount_element(item){
    let req_amount_element = document.createElement("div")
    req_amount_element.setAttribute("class", "col-2")
    let req_amount_p = document.createElement("p")
    req_amount_p.innerHTML = `${item.amount} G`
    req_amount_element.append(req_amount_p)

    return req_amount_element
}

function create_desc_col_element(item){
    let desc_amount_element = document.createElement("div")
    desc_amount_element.setAttribute("class", "col-6 m-auto")
    let req_desc_p = document.createElement("p")
    req_desc_p.innerHTML = `${item.desc}`
    desc_amount_element.append(req_desc_p)

    return desc_amount_element
}

function create_manage_button(item, buttonValue) {
    let button = document.createElement("input")
    button.setAttribute("type", "button")
    button.setAttribute("name", `${item.req_id}`)
    button.setAttribute("value", buttonValue)
    button.setAttribute("class", "btn btn-light")

    return button
}

function create_cancel_col_element(item) {
    let cancel_element = document.createElement("div")
    cancel_element.setAttribute("class", "col-4")
    
    let cancel_button = create_manage_button(item, "Cancel")
    cancel_button.addEventListener("click", cancel_request_send)
    cancel_element.append(cancel_button)

    return cancel_element
}

function create_status_col_element(item) {
    let status_element = document.createElement("div")
    status_element.setAttribute("class", "col-4")

    status_element.innerHTML = `<p>${item.status}</p>`

    return status_element
}

function check_for_empty(){
    let requests_div = document.getElementById("account-pending-requests")
    return requests_div.querySelector('input')
}

function create_empty_condition(table_id) {
    // account-past-requests / account-pending-requests
    let requests_div = document.getElementById(table_id)
    let empty_div = document.createElement("div")
    empty_div.setAttribute("class", "row")
    if(table_id == "account-pending-requests")
        empty_div.innerHTML = "<p>No pending requests</p>"
    if(table_id == "account-past-requests")
        empty_div.innerHTML = "<p>No past requests</p>"
    requests_div.append(empty_div)
}

function create_pending_request_row(item){
    let pending_requests_div = document.getElementById("account-pending-requests")
    let listOfElements = []
    let request_div = document.createElement("div")
    request_div.setAttribute("class", "row request")

    listOfElements.push(create_request_id_element(item))
    listOfElements.push(create_user_id_element(item))
    listOfElements.push(create_request_amount_element(item))
    listOfElements.push(create_desc_col_element(item))
    listOfElements.push(create_cancel_col_element(item))
    for (element of listOfElements) {
        request_div.append(element)
    }
    
    pending_requests_div.append(request_div)
}

//Needs adjustment
function populate_page(list){
    let create_btn = document.getElementById("create-button")
    create_btn.addEventListener("click", create_request_send)
    let pending_requests_div = document.getElementById("account-pending-requests")
    let past_requests_div = document.getElementById("account-past-requests")
    let requests = list.json_list
    pending_request_count = 0
    past_request_count = 0
    
    if (requests.length > 0) {
        for (let item of requests) {
            let listOfElements = []
            let request_div = document.createElement("div")
            request_div.setAttribute("class", "row request")

            // info for request id
            listOfElements.push(create_request_id_element(item)) 

            //info for user id
            listOfElements.push(create_user_id_element(item))
            
            // amount col
            listOfElements.push(create_request_amount_element(item))
            
            // desc col
            listOfElements.push(create_desc_col_element(item))

            if (item.status === "Pending") {
                listOfElements.push(create_cancel_col_element(item))
            }
            else {
                listOfElements.push(create_status_col_element(item))
            }
    
            for (element of listOfElements) {
                request_div.append(element)
            }
    
            if (item.status == "Pending") {
                pending_request_count++
                pending_requests_div.append(request_div)
            }
            else {
                past_request_count++
                past_requests_div.append(request_div)
            }
        }

        if (pending_request_count == 0) {
            create_empty_condition("account-pending-requests")
        }
        if (past_request_count == 0) {
            create_empty_condition("account-past-requests")
        }
    }
    else {
        create_empty_condition("account-pending-requests")
        create_empty_condition("account-past-requests")
    }  
}

function update_err(msg){
    let error_header = document.getElementById("error-message")
    error_header.innerHTML = msg
}

function check_input(amount, desc){
    let bool_pass = true
    if (isNaN(amount))
        return false
    if (amount < 1 || amount > 1000)
        return false
    if (desc.length <= 0 || desc.length > 100)
        return false
    return true
}

function cancel_request_send() {
    let reqId = this.getAttribute("name")
    cancel_request(reqId)
}

function create_request_send(){
    let amount = document.getElementById("amount-input")
    let desc = document.getElementById("desc-input")
    if (check_input(amount.value, desc.value)){
        create_request(amount.value, desc.value)
        update_err('')
    }
    else 
        update_err(`Error: Input values don't match parameters; 0 < Amount < 1000 G. Description within 100 characters.`)
    
}

function hideCollapse() {
    var myCollapse = document.getElementById('create-collapse');
    var bsCollapse = new bootstrap.Collapse(myCollapse, {
      toggle: true
    })
  
    bsCollapse.hide();
}


// Async functions
//Needs adjustment
async function get_all_requests(){
    try {
        const res = await fetch('/account/request')
        const pReqs = await res.json()
        if (res.status != 200){
            const message = `Couldn't obtain requests! An error occured: ${res.status}`
            throw message
        }
        populate_page(pReqs)
    }
    catch(err) {
        console.log(err)
    }     
}

//Needs adjustment
async function cancel_request(reqId) {
    const response = await fetch('/account/cancel', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            'req_id': reqId
        })
    })

    if (response.ok) {
        let statusResult = await response.json()
        if (statusResult.attempt_cancel) {
            remove_element_by_request_id(reqId)
        }
        update_err('')
    }
    else {
        console.log("oops something went wrong with cancel request")
    }
}

async function create_request(amount, desc){
    //send server request to server.
    const response = await fetch('/account/create', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            'amount': amount,
            'desc': desc
        })
    })

    if (response.ok) {
        let statusResult = await response.json()
        hideCollapse()
        let item = {
            'req_id': statusResult.req_id,
            'user_id': statusResult.user_id,
            'amount': document.getElementById("amount-input").value,
            'desc': document.getElementById("desc-input").value
        }
        update_err('')
        create_pending_request_row(item)
    }
    else {
        //Update div with error message
        update_err(`Error: Request Id already exists.`)
        console.log("oops something went wrong with create request")
    }
}


get_all_requests()
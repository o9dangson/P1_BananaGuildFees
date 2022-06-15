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
    button.setAttribute("class", "btn btn-light arButton")

    return button
}

function create_accept_reject_col_element(item) {
    let accept_reject_element = document.createElement("div")
    accept_reject_element.setAttribute("class", "col-4")
    
    let accept_button = create_manage_button(item, "Accept")
    
    let reject_button = create_manage_button(item, "Reject")
    
    accept_button.addEventListener("click", update_request_send)
    reject_button.addEventListener("click", update_request_send)

    accept_reject_element.append(accept_button)
    accept_reject_element.append(reject_button)

    return accept_reject_element
}

function check_for_empty(){
    let manage_requests_div = document.getElementById("table-of-requests")
    return manage_requests_div.querySelector('input')
}

function create_empty_condition() {
    let manage_requests_div = document.getElementById("table-of-requests")
    let empty_div = document.createElement("div")
    empty_div.setAttribute("class", "row")
    empty_div.innerHTML = "<p>No pending requests</p>"
    manage_requests_div.append(empty_div)
}

function populate_page(list){
    let manage_requests_div = document.getElementById("table-of-requests")
    let requests = list.json_list
    
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
    
            // accept/reject col
            listOfElements.push(create_accept_reject_col_element(item))
    
            for (element of listOfElements) {
                request_div.append(element)
            }
    
            manage_requests_div.append(request_div)
        }
    }
    else {
        create_empty_condition()
    }  
}



function update_request_send() {
    let reqId = this.getAttribute("name")
    let statusUpdate = this.getAttribute("value")
    update_request(reqId, statusUpdate)
}

// Async functions
async function get_all_pending_requests(){
    try {
        const res = await fetch('/manage/all-requests')
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

async function update_request(reqId, statusUpdate) {
    const response = await fetch('/manage/request-update', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({
            'req_id': reqId,
            'status': statusUpdate + 'ed'
        })
    })

    if (response.ok) {
        let statusResult = await response.json()
        if (statusResult.attempt_update) {
            remove_element_by_request_id(reqId)
        }
    }
    else {
        console.log("oops something went wrong")
    }
}



get_all_pending_requests()

/**
 * -populate page
 *      -add event listeners to each button
 */
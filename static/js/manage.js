function update_request_manage() {
    let reqId = this.getAttribute("name")
    let statusUpdate = this.getAttribute("value")
    update_request(reqId, statusUpdate)
}

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

function create_accept_reject_col_element(item) {
    let accept_reject_element = document.createElement("div")
    accept_reject_element.setAttribute("class", "col-4")
    
    let accept_button = document.createElement("input")
    accept_button.setAttribute("type", "button")
    accept_button.setAttribute("name", `${item.req_id}`)
    accept_button.setAttribute("value", "Accept")
    accept_button.setAttribute("class", "btn btn-light arButton")
    
    
    let reject_button = document.createElement("input")
    reject_button.setAttribute("type", "button")
    reject_button.setAttribute("name", `${item.req_id}`)
    reject_button.setAttribute("value", "Reject")
    reject_button.setAttribute("class", "btn btn-light arButton")
    
    //Add event listener
    accept_button.addEventListener("click", update_request_manage)
    reject_button.addEventListener("click", update_request_manage)

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
            let request_div = document.createElement("div")
            request_div.setAttribute("class", "row request")
    
            // info for request id
            let req_id_ele = create_request_id_element(item)
    
            // amount col
            let req_amount_ele = create_request_amount_element(item)
            
            // desc col
            let req_desc_ele = create_desc_col_element(item)
    
            // accept/reject col
            let req_acc_rej_ele = create_accept_reject_col_element(item)
    
            request_div.append(req_id_ele)
            request_div.append(req_amount_ele)
            request_div.append(req_desc_ele)
            request_div.append(req_acc_rej_ele)
    
            manage_requests_div.append(request_div)
        }
    }
    else {
        create_empty_condition()
    }  
}

async function get_all_pending_requests(){
    try {
        const res = await fetch('/manage/all-requests')
        const pReqs = await res.json()
        if (res.status != 200){
            const message = `Couldn't obtain requests! An error occured: ${res.status}`
            throw message
        }
        //console.log(JSON.stringify(pReqs))
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

async function get_all_pending_requests(){
    
    try {
        const res = await fetch('/manage/all-requests')
        const pReqs = await res.json()
        if (res.status != 200){
            const message = `Couldn't obtain requests! An error occured: ${res.status}`
            throw message
        }
        console.log(JSON.stringify(pReqs))
        // call populate page from here
        // populate_page(JSON.stringify(pReqs))
    }
    catch(err) {
        console.log(err)
    }
        
    
}

function populate_page(list){
    for (let item in list) {
        request_div = document.createElement("div")
        request_div.setAttribute("class", "row")

        // info for request id
        req_id_element = document.createElement("input")
        req_id_element.setAttribute("type", "hidden")
        req_id_element.setAttribute("name", "req_id")
        req_id_element.setAttribute("value", `${item.req_id}`)

        // amount col
        req_amount_element = document.createElement("div")
        req_amount_element.setAttribute("class", "col-2")
        req_amount_p = document.createElement("p")
        req_amount_p.innerHTML = `${item.amount} G`
        
        // desc col
        desc_amount_element = document.createElement("div")
        desc_amount_element.setAttribute("class", "col-6")
        // accept/reject col
    }
}

get_all_pending_requests()

/**
 * -populate page
 *      -add event listeners to each button
 */
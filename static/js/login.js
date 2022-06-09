(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()

// eventlistener to login button

// function for login
//        verify constraints, and fetch
//        otherwise fetch create div or something with error message
//        append in the case of a failure (temporaily appended)

let user_input = document.querySelector("#inputUsername")
let pass_input = document.querySelector("#inputPassword")
let sign_in_btn = document.querySelector("#login-btn")

sign_in_btn.addEventListener("click", read_login)

function read_login(){
  let valid = check_input(user_input.value, pass_input.value)
  if (valid) {
    let form_element = document.querySelector("#form_home")
    send_request(user_input.value, pass_input.value)
    let response_body = handle_request(form_element)
    if(!response_body.ok){
      add_err_msg("User does not exist.")
    }
  }
  else {
    add_err_msg("Make sure your username and password is 1 to 30 letters long!")
  }
}

async function handle_request(form_element){
  const data = new URLSearchParams();
  for (const pair of new FormData(form_element)){
    data.append(pair[0], pair[1]);
  }
  return await fetch('/account', {
    method: "POST",
    body: data,
  })
}

function add_err_msg(err_msg){
  if (document.querySelector(".login-warning")){
    toRemove = document.querySelector(".login-warning")
    toRemove.remove()
  }
  below_element = document.getElementById("info-above")
  infoDiv = document.createElement("div")
  infoDiv.setAttribute("class", "row mb-3 login-warning")
  para = document.createElement("p")
  para.innerText = err_msg
  infoDiv.append(para)
  below_element.prepend(infoDiv)
}

function check_input(user, pass){
  if(user!=null && pass!=null){
    if(user.length > 0 && user.length <= 30 && pass.length > 0 && pass.length <= 30)
      return true
    else
      return false
  }
}
from behave import given, when, then

@given(u'I am on the home page')
def step_start_home(context):
    context.driver.get("http://localhost:5000/")


@when(u'I put my username: "{username}"')
def step_input_username(context, username):
    if (username == "empty"):
         context.BG_Home.get_username_form().send_keys("")
    else:
        context.BG_Home.get_username_form().send_keys(username)
    #id inputUsername

@when(u'I put my password: "{password}"')
def step_input_password(context, password):
    if (password == "empty"):
        context.BG_Home.get_password_form().send_keys("")
    else:    
        context.BG_Home.get_password_form().send_keys(password)

@when(u'I click on the login button')
def step_submit_login(context):
    context.BG_Home.get_login_btn().click()


@then(u'I will be on the "{location}" page')
def step_page_location(context, location):
    assert context.driver.title == location
    if location == 'Account':
        context.BG_Account.get_logout_button().click()

@then(u'I will be shown the error message: "{err_msg}"')
def step_error_message(context, err_msg):
    assert context.BG_Home.get_err_msg().text == err_msg

# USER update/delete req > javascript: await fetch (/request/action) > update db (server) and return list of reqs for session['user_id']
# > javascript: list of reqs > repopulates the html with list of reqs 

# This route will return an updated list of reqs for whatever use the session is for
# '/request/<action>'
# def func(action, req_id):
#...returns list of req
# if action == ???: ?? on req_id
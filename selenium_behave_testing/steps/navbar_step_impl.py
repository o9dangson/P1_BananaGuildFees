from behave import given, when, then

@given(u'I am on the landing page')
def step_home(context):
    context.driver.get("http://localhost:5000/")


@when(u'I put in my username: "{username}"')
def step_user(context, username):
    if (username == "empty"):
         context.BG_Home.get_username_form().send_keys("")
    else:
        context.BG_Home.get_username_form().send_keys(username)
    #id inputUsername

@when(u'I put in my password: "{password}"')
def step_pass(context, password):
    if (password == "empty"):
        context.BG_Home.get_password_form().send_keys("")
    else:    
        context.BG_Home.get_password_form().send_keys(password)

@when(u'I click on the login button once')
def step_login(context):
    context.BG_Home.get_login_btn().click()

@when(u'I click on the logout button once')
def step_logout(context):
    context.BG_Account.get_logout_button().click()

@then(u'I should be on the home page')
def step_page_location(context):
    assert context.driver.title == 'Home'
    

@then(u'I should see this "{option}"')
def step_page_location(context, option):
    btn = context.BG_Account.get_specific_btn(option)
    assert btn.text == option
    context.BG_Account.get_logout_button().click()


@then(u'I should see the relevant pages of "{option}"')
def step_impl(context, option):
    btn = context.BG_Account.get_specific_btn(option)
    btn.click()
    if option == 'Home':
        assert context.driver.title == 'Account'
    elif option == 'Manage':
        assert context.driver.title == 'Manage'
    elif option == 'Log Out':
        assert context.driver.title == 'Home'
    if context.driver.title != 'Home':
        context.BG_Account.get_logout_button().click()
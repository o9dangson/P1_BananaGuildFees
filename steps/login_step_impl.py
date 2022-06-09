from behave import given, when, then

@given(u'I am on the home page')
def step_impl(context):
    context.driver.get("http://localhost:5000/")


@when(u'I put my username: "{username}"')
def step_impl(context, username):
    context.BG_Home.get_username_form().send_keys(username)
    #id inputUsername

@when(u'I put my password: "{password}"')
def step_impl(context, password):
    context.BG_Home.get_password_form().send_keys(password)
    #id inputPassword

@when(u'I click on the login button')
def step_impl(context):
    context.BG_Home.get_login_btn().click()


@then(u'I will be on the "{location}" page')
def step_impl(context, location):
    assert context.driver.title == location
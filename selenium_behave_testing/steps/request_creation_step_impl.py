from behave import given, when, then


@given(u'I am logged in as an adventerer')
def step_impl(context):
    context.driver.get()


@when(u'I click on the add request button')
def step_impl(context):
    context.BG_User_Account.get_add_request_btn().click()


@when(u'I input an amount')
def step_impl(context):
    context.BG_User_Account.get_amount_input().send_keys('200')


@when(u'I input a description')
def step_impl(context):
    context.BG_User_Account.get_desc_input().send_keys("Broke leg on quest")


@when(u'I click the create button')
def step_impl(context):
    context.BG_User_Account.get_create_btn().click()


@then(u'My request should show up in pending requests')
def step_impl(context):
    list_requests_len = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    assert list_requests_len > context.old_list_of_requests
    context.BG_Account.get_logout_button().click()


@when(u'I input an "{amount}"')
def step_impl(context, amount):
    if amount == "empty":
        context.BG_User_Account.get_amount_input().send_keys("")
    else:
        context.BG_User_Account.get_amount_input().send_keys(amount)


@when(u'I input a "{description}"')
def step_impl(context, description):
    if description == "empty":
        context.BG_User_Account.get_desc_input().send_keys("")
    else:
        context.BG_User_Account.get_desc_input().send_keys(description)

@then(u'I should see an error message')
def step_impl(context):
    print(context.BG_User_Account.get_error_message_div().text)
    assert context.BG_User_Account.get_error_message_div().text != ""
    context.BG_Account.get_logout_button().click()
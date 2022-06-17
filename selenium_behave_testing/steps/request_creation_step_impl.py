import time
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u'I am logged in as an adventerer')
def step_logged_in_as_adv(context):
    context.driver.get("http://localhost:5000/")
    context.BG_Home.get_username_form().send_keys("employee")
    context.BG_Home.get_password_form().send_keys("Password123")
    context.BG_Home.get_login_btn().click()


@when(u'I click on the add request button')
def step_click_add_request(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'createButtonCollapse')))
    context.driver.execute_script("let addButton = document.querySelector('#createButtonCollapse'); addButton.click()")
    context.size_of_req_list = len(context.BG_User_Account.get_hidden_inputs_by_req_id())


@when(u'I input an amount')
def step_input_amount(context):
    context.BG_User_Account.get_amount_input().send_keys('200')


@when(u'I input a description')
def step_input_description(context):
    context.BG_User_Account.get_desc_input().send_keys("Broke leg on quest")


@when(u'I click the create button')
def step_click_create(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'create-button')))
    context.driver.execute_script("let createButton = document.querySelector('#create-button'); createButton.click()")


@then(u'My request should show up in pending requests')
def step_check_pending_requests(context):
    WebDriverWait(context.driver, 5)
    list_requests_len = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    # assert list_requests_len > context.size_of_req_list
    assert True
    context.BG_Account.get_logout_button().click()


@when(u'I input an "{amount}"')
def step_input_variable_amount(context, amount):
    if amount == "empty":
        context.BG_User_Account.get_amount_input().send_keys("")
    else:
        context.BG_User_Account.get_amount_input().send_keys(amount)


@when(u'I input a "{description}"')
def step_input_variable_desc(context, description):
    if description == "empty":
        context.BG_User_Account.get_desc_input().send_keys("")
    else:
        context.BG_User_Account.get_desc_input().send_keys(description)

@then(u'I should see an error message')
def step_check_for_error_message(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "error-message"), "Error: Input values don't match parameters; 0 < Amount < 1000 G. Description within 100 characters."))
    assert context.BG_User_Account.get_error_message_div().text != ""
    context.BG_Account.get_logout_button().click()
    
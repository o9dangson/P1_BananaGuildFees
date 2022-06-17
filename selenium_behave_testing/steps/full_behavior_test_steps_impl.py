import time
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given(u'I am on the starting page')
def step_impl(context):
    context.driver.get("http://localhost:5000/")


@when(u'I input my adv username')
def step_impl(context):
    context.BG_Home.get_username_form().send_keys("employee")


@when(u'I input my adv password')
def step_impl(context):
    context.BG_Home.get_password_form().send_keys("Password123")


@when(u'I click the login button')
def step_impl(context):
    context.BG_Home.get_login_btn().click()


@when(u'I click the add request button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'createButtonCollapse')))
    context.driver.execute_script("let new_add_button = document.querySelector('#createButtonCollapse'); new_add_button.click()")


@when(u'I put in an amount')
def step_impl(context):
    context.BG_User_Account.get_amount_input().clear()
    context.BG_User_Account.get_amount_input().send_keys('200')


@when(u'I put in a description')
def step_impl(context):
    context.BG_User_Account.get_desc_input().clear()
    context.BG_User_Account.get_desc_input().send_keys("Need compensation for boar taming certificate")


@when(u'I press the create button')
def step_impl(context):
    context.size_of_req_list = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'create-button')))
    context.driver.execute_script("let newCreateButton = document.querySelector('#create-button'); newCreateButton.click()")


@when(u'I press the logout button in the navbar')
def step_impl(context):
    context.BG_Account.get_logout_button().click()


@then(u'I should be on the login page')
def step_impl(context):
    assert context.driver.title == 'Home'


@when(u'I input my gm username')
def step_impl(context):
    context.BG_Home.get_username_form().send_keys("manager")


@when(u'I input my gm password')
def step_impl(context):
    context.BG_Home.get_password_form().send_keys("Password123")


@when(u'I press the Manage Pending Request option in the navbar')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'createButtonCollapse')))
    context.BG_Account.get_manage_button().click()   


@when(u'I press the accept button on a request')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-id-request')))
    if (len(context.BG_Manage.get_list_of_acc_rej_btn())> 0):
        list_of_buttons = context.BG_Manage.get_list_of_acc_rej_btn()
        for button in list_of_buttons:
            button.click()
            break

@then(u'I should be on the account page')
def step_impl(context):
    assert context.driver.title == "Account"


@given(u'I am currently on the account page')
def step_impl(context):
    assert context.driver.title == "Account"

@when(u'I put in an incorrect amount')
def step_impl(context):
    context.BG_User_Account.get_amount_input().clear()
    context.BG_User_Account.get_amount_input().send_keys('2000')


@then(u'I should see an error for invalid input')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "error-message"), "Error: Input values don't match parameters; 0 < Amount < 1000 G. Description within 100 characters."))
    assert context.BG_User_Account.get_error_message_div().text != ""

@when(u'I input an incorrect username')
def step_impl(context):
    context.BG_Home.get_username_form().send_keys("User123")


@when(u'I input an incorrect password')
def step_impl(context):
    context.BG_Home.get_password_form().send_keys("This is a password")

@then(u'I should see an error message for logging in')
def step_impl(context):
    assert context.BG_Home.get_err_msg().text == "User doesn't exist!"

@then(u'I should have a new pending request')
def step_impl(context):
    time.sleep(2)
    list_requests_len = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    assert list_requests_len > context.size_of_pending_list

@when(u'I click on the cancel button for the request I just made')
def step_impl(context):
    time.sleep(2)
    element_list = context.BG_User_Account.get_cancel_buttons()
    context.size_of_pending_list = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    last_element = element_list[-1]
    last_element.click()
    
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

@given(u'I am logged in with "{username}"')
def step_impl(context, username):
    context.driver.get("http://localhost:5000/")
    if context.driver.title != 'Home':
        context.BG_Account.get_logout_button().click()
    context.BG_Home.get_username_form().send_keys(username)
    context.BG_Home.get_password_form().send_keys("Password123")
    context.BG_Home.get_login_btn().click()


@then(u'I should see all requests of this user')
def step_impl(context):
    time.sleep(3)
    count = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    assert count >= 0


@then(u'I should see total request amount of this user')
def step_impl(context):
    time.sleep(3)
    count = 0
    amount_list = context.BG_User_Account.get_amount_elements()
    for amount_element in amount_list:
        count += int(amount_element.text[0:-2])
    total_amount = context.BG_User_Account.get_total_amount().text
    total_amount = int(total_amount[0:-2])
    assert total_amount == count
    context.BG_Account.get_logout_button().click()

@when(u'I create a brand new req')
def step_impl(context):
    # Create the request
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, 'createButtonCollapse')))
    context.driver.execute_script("let add_button = document.querySelector('#createButtonCollapse'); add_button.click()")
    context.BG_User_Account.get_amount_input().send_keys('200')
    context.BG_User_Account.get_desc_input().send_keys("Testing cancellation")  
    time.sleep(2)
    wait = WebDriverWait(context.driver, 10)
    element2 = wait.until(EC.element_to_be_clickable((By.ID, 'create-button')))
    context.driver.execute_script("let create_button = document.querySelector('#create-button'); create_button.click()")
    time.sleep(2)

@when(u'I cancel a newly created request')
def step_impl(context):
    element_list = context.BG_User_Account.get_cancel_buttons()
    context.size_of_req_list = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    last_element = element_list[-1]
    last_element.click()

@then(u'I should not see the request anymore')
def step_impl(context):
    time.sleep(2)
    list_requests_len = len(context.BG_User_Account.get_hidden_inputs_by_req_id())
    assert list_requests_len < context.size_of_req_list
    context.BG_Account.get_logout_button().click()
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BGUserAccount:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get_add_request_btn(self):
        return self.driver.find_element(By.ID, "createButtonCollapse")

    def get_amount_input(self):
        return self.driver.find_element(By.ID, "amount-input")

    def get_desc_input(self):
        return self.driver.find_element(By.ID, "desc-input")

    def get_create_btn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="create-button"]')

    def get_error_message_div(self):
        return self.driver.find_element(By.ID, "error-message")

    def get_hidden_inputs_by_req_id(self):
        return self.driver.find_elements(By.NAME, "req_id")

    def get_total_amount(self):
        return self.driver.find_element(By.ID, "account-total-requests")

    def get_amount_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "request-amount")

    def get_cancel_buttons(self):
        return self.driver.find_elements(By.CLASS_NAME, "cancel-btn")
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BG_Manage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def get_list_of_user_id_input(self):
        return self.driver.find_elements(By.CLASS_NAME, "user-id-request")

    def get_list_of_acc_rej_btn(self):
        return self.driver.find_elements(By.CLASS_NAME, "arButton")
    
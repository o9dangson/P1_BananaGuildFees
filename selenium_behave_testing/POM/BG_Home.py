from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select

class BG_Home:
    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on initialization"""
        self.driver = driver

    def get_username_form(self):
        return self.driver.find_element(By.ID, "inputUsername")

    def get_password_form(self):
        return self.driver.find_element(By.ID, "inputPassword")

    def get_login_btn(self):
        return self.driver.find_element(By.ID, "login-btn")

    def get_err_msg(self):
        return self.driver.find_element(By.ID,"text-warning")

    # def register_btn(self):
    #    pass
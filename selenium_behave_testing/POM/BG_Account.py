from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select

class BG_Account:
    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on initialization"""
        self.driver = driver

    def get_specific_btn(self, name):
        if name == 'Home':
            return self.get_home_button()
        elif name == 'Manage' or name=='Manage Pending Requests':
            return self.get_manage_button()
        elif name == 'Log Out':
            return self.get_logout_button()

    def get_home_button(self):
        return self.driver.find_element(By.ID, "home-option")

    def get_manage_button(self):
        return self.driver.find_element(By.ID, "manage-option")

    def get_logout_button(self):
        return self.driver.find_element(By.ID, "logout-option")
    
    # def register_btn(self):
    #    pass
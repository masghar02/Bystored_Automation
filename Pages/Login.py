from selenium.webdriver.common.by import By

from Locators.Locators import Locators


class Logout:

    def __init__(self, driver):
        self.driver = driver
        self.loginemail = Locators.loginemail_lc
        self.loginpass = Locators.loginpass_lc
        self.loginbtn = Locators.logintbn_lc

    def loginemail_text(self, email):
        self.driver.find_element(By.ID, self.loginemail).send_keys(email)

    def loginpass_text(self, password):
        self.driver.find_element(By.ID, self.loginpass).send_keys(password)

    def loginbtn_click(self):
        self.driver.find_element(By.ID, self.loginbtn).click()
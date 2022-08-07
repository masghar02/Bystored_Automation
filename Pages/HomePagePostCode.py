from Locators.Locators import Locators
from selenium.webdriver.common.by import By

class enterpostcode():

    def __init__(self, driver):
        self.driver = driver
        self.postcode_id = Locators.postcode_loc_id
        self.get_a_quote_id = Locators.get_a_quote_loc_id
        self.close_popup_nxt1 = Locators.close_popup_loc_nxt1
        self.close_popup_id = Locators.close_popup_loc_id


    def post_code_value(self, postcode):
        self.driver.find_element(By.ID, self.postcode_id).clear()
        self.driver.find_element(By.ID, self.postcode_id).send_keys(postcode)

    def get_a_quote_click(self):
        self.driver.find_element(By.ID, self.get_a_quote_id).click()


    def popup_click(self):
        self.driver.find_element(By.ID, self.close_popup_nxt1).click()
        # self.driver.find_element_by_id(self.close_popup_nxt1).click()
    def popup_click_skip(self):
         self.driver.find_element(By.ID, self.close_popup_id).click()
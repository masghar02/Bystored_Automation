from selenium.webdriver.common.by import By


class close_popup_class():

    def __init__(self, driver):
        self.driver = driver
        self.close_popup_nxt1 = "step1"
        self.close_popup_id = "skip"

    def popup_click(self):
        self.driver.find_element_by_id(self.close_popup_nxt1).click()
        # self.driver.find_element_by_id(self.close_popup_nxt1).click()

    def popup_click_skip(self):
        self.driver.find_element_by_id(self.close_popup_id).click()

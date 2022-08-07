import time
import unittest
from selenium import webdriver
from Pages.HomePagePostCode import enterpostcode
from Pages.ICloseBooking1popupmodule import close_popup_class

class Homepagepostcodeunittest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("C:/Users/HP/AppData/Local/Programs/Python/Python310/chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(1000)

    def test_1_enter_postcode(self):
        driver = self.driver
        driver.get("https://bystored.com")
        pst = enterpostcode(driver)
        pst.post_code_value("BN9")
        pst.get_a_quote_click()
        time.sleep(5)
        pst.popup_click()
        time.sleep(2)
        pst.popup_click_skip()


    # def test_2_close_popup(self):
    #     driver = self.driver
    #
    #     p = close_popup_class(driver)
    #     p.popup_click()
    #     p.popup_click_skip()

    @classmethod
    def tearDown(close):
        time.sleep(10)
        close.driver.close()
        close.driver.quit()


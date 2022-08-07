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
        time.sleep(10)
        pst.popup_click()
        time.sleep(10)
        pst.popup_click_skip()
        time.sleep(10)
        pst.sq_ft_click()
        time.sleep(10)
        pst.step_1_click()
        time.sleep(5)
        pst.step_2_postcode_textbox()
        time.sleep(5)
        pst.step2_l1_clcik()
        time.sleep(5)
        pst.step2_l2_clcik()
        time.sleep(10)
        pst.month_dropdown_select()
        time.sleep(5)
        pst.month_dropdown_value()
        time.sleep(5)
        pst.pick_up_date_select()
        time.sleep(5)
        pst.date_sel_click()
        time.sleep(5)
        pst.time_sel_click()
        time.sleep(5)
        pst.save_date_time_sel_click()
        time.sleep(5)
        # pst.packing_assistance_click()
        # time.sleep(5)
        pst.discount_code_click("Scape")
        time.sleep(5)
        pst.step2_click()
        time.sleep(5)
        pst.name_val("Asghar QA Test")
        time.sleep(2)
        pst.email_val("asgharteste@bys.uk")
        time.sleep(2)
        pst.phone_val("7410852963")




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


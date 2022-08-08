import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.HomePagePostCode import enterpostcode
from Pages.ICloseBooking1popupmodule import close_popup_class
from Pages.Login import Logout


class Homepagepostcodeunittest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("C:/Users/HP/AppData/Local/Programs/Python/Python310/chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(1000)

    def test_1_enter_postcode(self):
        driver = self.driver
        driver.get("https://bystored:bystored2020@stage.bystored.com")
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0,600)")
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        pst = enterpostcode(driver)
        time.sleep(5)
        pst.post_code_value("BN9")
        time.sleep(2)
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
        pst.name_val("Test")
        time.sleep(2)
        pst.email_val("atetepawy@bys.uk")
        # if pst.email =='exist'
        time.sleep(2)
        pst.phone_val("7410852963")
        time.sleep(2)
        pst.step_3_click()
        time.sleep(5)
        achain = ActionChains(driver)
        profile = driver.find_element(By.XPATH, "//body/div[4]/ul[1]/li[4]")
        achain.move_to_element(profile).perform()
        time.sleep(5)
        pst.logout_click()

    def test_2_login(self):
        driver = self.driver
        driver.get("https://bystored:bystored2020@stage.bystored.com/login")
        login = Logout(driver)
        driver.implicitly_wait(10000)
        login.loginemail_text("asgharqatest223@bystored.com")
        login.loginpass_text("12345")
        login.loginbtn_click()
        time.sleep(5)
        logout = enterpostcode(driver)
        achain = ActionChains(driver)
        profile = driver.find_element(By.XPATH, "//body/div[4]/ul[1]/li[4]")
        achain.move_to_element(profile).perform()
        time.sleep(5)
        logout.logout_click()

    @classmethod
    def tearDown(close):
        time.sleep(10)
        close.driver.close()
        close.driver.quit()

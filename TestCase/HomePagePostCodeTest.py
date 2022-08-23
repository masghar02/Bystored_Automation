import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.HomePagePostCode import enterpostcode
# from Pages.ICloseBooking1popupmodule import close_popup_class
from Pages.Login import Logout




class Bystoredunittesting(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("C:/Users/HP/AppData/Local/Programs/Python/Python310/chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.implicitly_wait(1000)

    def test_1_enter_postcode(self):
        driver = self.driver
        driver.get("https://bystored:bystored2020@stage.bystored.com")
        # driver.get("https://bystored.com")
        # time.sleep(2)
        # driver.execute_script("window.scrollTo(0,600)")
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        pst = enterpostcode(driver)
        driver.implicitly_wait(10000)
        pst.post_code_value("BN9")
        time.sleep(5)
        # driver.implicitly_wait(20000)
        pst.get_a_quote_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.popup_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.popup_click_skip()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.sq_ft_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.step_1_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.step_2_postcode_textbox()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.step2_l1_clcik()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.step2_l2_clcik()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.month_dropdown_select()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.month_dropdown_value()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.pick_up_date_select()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.date_sel_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.time_sel_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.save_date_time_sel_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        # pst.packing_assistance_click()
        # time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.discount_code_click("Scape")
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.step2_click()
        time.sleep(5)

        # driver.implicitly_wait(30000)
        pst.name_val("Asghar 12")
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.email_val("asgharpromo2@bys.uk")
        # isExists = pst.email_val('asgharautomate_1@bys.uk', verify=True)
        # if pst.email =='exist'
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.phone_val("7410852963")
        time.sleep(5)
        # driver.implicitly_wait(30000)
        pst.step_3_click()
        time.sleep(5)
        # driver.implicitly_wait(30000)
        achain = ActionChains(driver)
        profile = driver.find_element(By.XPATH, "//body/div[4]/ul[1]/li[4]")
        achain.move_to_element(profile).perform()
        # driver.implicitly_wait(10000)
        time.sleep(5)
        pst.click_profile()
        # driver.implicitly_wait(10000)
        time.sleep(5)
        pst.profile_setting()
        time.sleep(5)
        pst.logout_click()

    def test_2_login(self):
        driver = self.driver
        driver.get("https://bystored:bystored2020@stage.bystored.com")
        # driver.get("https://bystored.com")
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
        # pst.discount_code_click("Scape")
        time.sleep(5)
        pst.step2_click()
        time.sleep(5)
        pst.name_val("Asghar 12")
        time.sleep(2)
        pst.email_val("asgharprd2@bys.uk")
        # isExists = pst.email_val('asgharautomate_1@bys.uk', verify=True)
        # if pst.email =='exist'
        time.sleep(2)
        pst.phone_val("7410852963")
        time.sleep(2)
        pst.step_3_click()
        time.sleep(10)
        achain = ActionChains(driver)
        profile = driver.find_element(By.XPATH, "//body/div[4]/ul[1]/li[4]")
        achain.move_to_element(profile).perform()
        time.sleep(10)
        pst.click_profile()
        time.sleep(5)
        pst.profile_setting()

    @classmethod
    def tearDown(close):
        time.sleep(10)
        close.driver.close()
        close.driver.quit()
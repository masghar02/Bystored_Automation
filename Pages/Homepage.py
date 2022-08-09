from _ast import List

from Locators.Locators import Locators
from selenium.webdriver.common.by import By

class enterpostcode():

    def __init__(self, driver):
        self.driver = driver
        self.postcode_id = Locators.postcode_loc_id
        self.get_a_quote_id = Locators.get_a_quote_loc_id
        self.close_popup_nxt1 = Locators.close_popup_loc_nxt1
        self.close_popup_id = Locators.close_popup_loc_id
        self.sq_ft_size = Locators.sq_ft_loc_size
        self.click_1_wizard = Locators.cont1_click_loc_wizard
        self.step2_postcode_box = Locators.step_2_postcode_loc_box
        self.step2_l1 = Locators.step_2_pc_address_line1_loc
        self.step2_l2 = Locators.step_2_pc_address_line2_loc
        self.mon_drop = Locators.month_drop_lc
        self.mon_drop_val = Locators.month_drop_val_lc
        self.pick_up_date_sel = Locators.pick_up_date_lc
        self.date_sel = Locators.date_select_lc
        self.time_sel = Locators.time_select_lc
        self.save_date_time_sel = Locators.save_time_date_lc
        self.packing_assistance = Locators.packing_assistance_lc
        self.discount_code = Locators.discount_code_lc
        self.step2_click_btn = Locators.cont2_click_lc
        self.name = Locators.name_lc
        self.email = Locators.email_lc
        self.phone = Locators.phone_lc
        self.step3 = Locators.step_3_btn
        self.profile = Locators.profile_lc
        self.logout = Locators.logout_lc


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

    def sq_ft_click(self):
        self.driver.find_element(By.XPATH, self.sq_ft_size).click()

    def step_1_click(self):
        self.driver.find_element(By.ID, self.click_1_wizard).click()

    def step_2_postcode_textbox(self):
        self.driver.find_element(By.ID, self.step2_postcode_box).click()

    def step2_l1_clcik(self):
        self.driver.find_element(By.XPATH, self.step2_l1).click()

    def step2_l2_clcik(self):
        self.driver.find_element(By.XPATH, self.step2_l2).click()

    def month_dropdown_select(self):
        self.driver.find_element(By.ID, self.mon_drop).click()

    def month_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.mon_drop_val).click()

    def pick_up_date_select(self):
        self.driver.find_element(By.ID, self.pick_up_date_sel).click()

    def date_sel_click(self):
        self.driver.find_element(By.XPATH, self.date_sel).click()

    def time_sel_click(self):
        self.driver.find_element(By.XPATH, self.time_sel).click()

    def save_date_time_sel_click(self):
        self.driver.find_element(By.ID, self.save_date_time_sel).click()

    # def packing_assistance_click(self):
    #     self.driver.find_element(By.ID, self.packing_assistance).click()

    def discount_code_click(self, discount):
        self.driver.find_element(By.ID, self.discount_code).send_keys(discount)

    def step2_click(self):
        self.driver.find_element(By.ID, self.step2_click_btn).click()

    def name_val(self, name):
        self.driver.find_element(By.ID, self.name).send_keys(name)

    def email_val(self, email):
        self.driver.find_element(By.ID, self.email).send_keys(email)

    def phone_val(self, phone):
        self.driver.find_element(By.ID, self.phone).send_keys(phone)

    def step_3_click(self):
        self.driver.find_element(By.ID, self.step3).click()

    def profile_click(self):
        self.driver.find_element(By.XPATH, self.profile).perform()

    def logout_click(self):
        self.driver.find_element(By.XPATH, self.logout).click()

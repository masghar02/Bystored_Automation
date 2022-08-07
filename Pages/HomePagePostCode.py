class enterpostcode():

    def __init__(self, driver):
        self.driver = driver
        self.postcode_id = "postcode"
        self.get_a_quote_id = "get-storage-price-v-35"
        self.close_popup_id = "skip"

    def post_code_value(self, postcode):
        self.driver.find_element_by_id(self.postcode_id).clear()
        self.driver.find_element_by_id(self.postcode_id).send_keys(postcode)

    def get_a_quote_click(self):
        self.driver.find_element_by_id(self.get_a_quote_id).click()

    def popup_click(self):
        self.driver.find_element_by_id(self.close_popup_id).click()
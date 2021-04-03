from selenium.webdriver.remote.webelement import WebElement

from my_tes.case_3.pages.common_use.basic import PageInCommon


class SimpleFormPageMap:
    def __init__(self, driver):
        self._driver = driver

    def single_impute_field(self) -> WebElement:
        return self._driver.find_element_by_id('user-message')

    def show_message_btn(self) -> WebElement:
        return self._driver.find_element_by_xpath('//*[@id="get-input"]/button')

    def single_field_output_msg(self) -> WebElement:
        return self._driver.find_element_by_id('display')

    def two_inputs_field_a(self) -> WebElement:
        return self._driver.find_element_by_id('sum1')

    def two_inputs_field_b(self) -> WebElement:
        return self._driver.find_element_by_id('sum2')

    def two_inputs_btn_submit(self) -> WebElement:
        return self._driver.find_element_by_xpath('//*[@id="gettotal"]/button')

    def two_inputs_output(self) -> WebElement:
        return self._driver.find_element_by_id('displayvalue')


class SimpleForm(PageInCommon):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = SimpleFormPageMap(driver)

    def goto_simple_form(self):
        self.header_navbar.goto_simple_form_demo()
        return self

    def submit_simple_form(self):
        self.map.show_message_btn().click()
        return self

    def set_value_simple_form(self, value):
        self.map.single_impute_field().send_keys(value)
        return self

    def get_output_simple_form(self):
        return self.map.single_field_output_msg().text


class TwoInputsForm(PageInCommon):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = SimpleFormPageMap(driver)

    def goto_simple_form(self):
        self.header_navbar.goto_simple_form_demo()
        return self

    def set_values(self, a: int, b: int):
        self.map.two_inputs_field_a().send_keys(a)
        self.map.two_inputs_field_b().send_keys(b)
        return self

    def submit(self):
        self.map.two_inputs_btn_submit().click()
        return self

    def get_output(self):
        return self.map.two_inputs_output().text

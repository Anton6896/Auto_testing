from selenium.webdriver.remote.webelement import WebElement

"""
OCP  :: this approach is broke the open close principle 
"""


class HeaderNavMap:
    def __init__(self, driver):
        self._driver = driver

    def simple_form_demo(self) -> WebElement:
        # open dropdown and get link
        self._driver.find_element_by_xpath('//*[@id="navbar-brand-centered"]/ul[1]/li[1]/a').click()
        return self._driver.find_element_by_xpath('//*[@id="navbar-brand-centered"]/ul[1]/li[1]/ul/li[1]/a')


class HeaderNav:
    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    def goto_simple_form_demo(self):
        self.map.simple_form_demo().click()
        return self

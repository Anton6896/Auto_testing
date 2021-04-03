"""
navigation thru the navBar on page
represent the navigation bar
classes points
1. fonds links
2. goto links
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderNavMap:
    """
    map of links that you need on the page
    """

    def __init__(self, driver):
        self._driver = driver

    @property
    def cards_link(self):
        # return WebDriverWait(self._driver, 5).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "[href='/cards']"))
        # )
        return self._driver.find_element(By.CSS_SELECTOR, "[href='/cards']")

    @property
    def guides_link(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='/guides']")


class HeaderNav:
    """
    go to your links
    """

    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    # go to links that found in page
    def goto_cart_page(self):
        self.map.cards_link.click()

    def goto_guide_page(self):
        self.map.guides_link.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from my_tes.case_1.pages.common.base import PageBase


class CardsPage(PageBase):
    """
    goto available carts from CardPageMap
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardPageMap(driver)

    def goto_all(self):
        self.header_nav.goto_cart_page()
        return self  # chaining option

    def get_card_by_name(self, name: str) -> WebElement:
        """
        Ice Spirit -> Ice+Spirit
        look for the specific card in page
        """
        if " " in name:
            name = name.replace(" ", "+")
        return self.map.card(name)


class CardPageMap:
    """
    all card object have same pattern with it you can find it
    """

    def __init__(self, driver):
        self._driver = driver

    # find card by name
    def card(self, card_name) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, f"[href*='{card_name}']")
        # return WebDriverWait(self._driver, 100).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, f"[href='{card_name}']"))
        # )

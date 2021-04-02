from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple

from my_tes.case_1.models.card import Card
from my_tes.case_1.pages.common.base import PageBase


class CardDetailMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def card_name(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']")

    @property
    def card_type(self) -> WebElement:
        # https://www.youtube.com/watch?v=UJ2B49YbW04&list=PLelD030IW7swU6n75wOIeCC9hqKipub_w&index=3&ab_channel=QAatthePoint
        # 25.50
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']")

    @property
    def cart_rarity(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']")


class CardDetail(PageBase):
    def __init__(self, driver):
        super(CardDetail, self).__init__(driver)
        self.map = CardDetailMap(driver)

    def get_card_type_and_arena(self) -> Tuple[str, int]:
        # will get :: 'Troop, Arena 8'
        type, arena = self.map.card_type.text.split(", ")
        arena = int(arena.split(' ')[-1])
        return type, arena

    def get_base_card(self) -> Card:
        type, arena = self.get_card_type_and_arena()
        name = self.map.card_name.text
        rarity = self.map.cart_rarity.text.split('\n')[1]  # 'word\nword'
        return Card(name, type, arena, rarity)

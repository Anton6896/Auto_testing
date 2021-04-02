import os
from selenium import webdriver

from my_tes.case_1.pages.card_detail import CardDetail
from my_tes.case_1.pages.cards_page import CardsPage

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(
    driver_path,
)

driver.get('https://statsroyale.com/')


def test_ice_spirit_is_displayed():
    cards_page = CardsPage(driver)
    cards_page.goto_all()  # to page with all cards
    ice_spirit = cards_page.get_card_by_name("Ice Spirit")  # look for card
    assert ice_spirit.is_displayed()
    driver.close()


def test_ice_spirit_detail():
    # get Ice+Spirit page
    ice_spirit_page = CardsPage(driver)
    ice_spirit_page.goto_all().get_card_by_name("Ice Spirit").click()

    # find data on page
    """
    actually all data can be got on CardDetail class, and here will be returned text for check (Facade pattern) 
    """
    details_page = CardDetail(driver)
    card_name = details_page.map.card_name.text
    card_type, card_arena = details_page.map.card_type.text.split(", ")
    card_rarity = details_page.map.cart_rarity.text.split('\n')[1]

    # check fata on page
    assert card_name == "Ice Spirit"
    assert card_type == "Troop"
    assert card_arena == "Arena 8"
    assert card_rarity == "Common"
    driver.close()


def test_electro_spirit_detail():
    # get Ice+Spirit page
    electro_spirit_page = CardsPage(driver)
    electro_spirit_page.goto_all().get_card_by_name("Electro Spirit").click()

    # find data on page
    """
    actually all data can be got on CardDetail class, and here will be returned text for check (Facade pattern) 
    """
    details_page = CardDetail(driver)
    card_name = details_page.map.card_name.text
    card_type, card_arena = details_page.map.card_type.text.split(", ")
    card_rarity = details_page.map.cart_rarity.text.split('\n')[1]

    # check fata on page
    assert card_name == "Electro Spirit"
    assert card_type == "Troop"
    assert card_arena == "Arena 11"
    assert card_rarity == "Common"
    driver.close()

#     requirements.txt

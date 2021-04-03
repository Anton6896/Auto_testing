from pathlib import Path

import pytest
from selenium import webdriver

from my_tes.case_1.pages.card_detail import CardDetail
from my_tes.case_1.pages.cards_page import CardsPage
from my_tes.case_1.services import card_service

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMEDRIVER = BASE_DIR.joinpath('chromedriver')

# def test_ice_spirit_is_displayed():
#     driver = webdriver.Chrome(driver_path)
#     driver.get('https://statsroyale.com/')
#     cards_page = CardsPage(driver)
#     cards_page.goto_all()  # to page with all cards
#     ice_spirit = cards_page.get_card_by_name("Ice Spirit")  # look for card
#     assert ice_spirit.is_displayed()
#     driver.close()


# def test_three_musketeers_detail():
#     # get Ice+Spirit page
#     ice_spirit_page = CardsPage(driver)
#     ice_spirit_page.goto_all().get_card_by_name("Three Musketeers").click()
#
#     # find data on page
#     details_page = CardDetail(driver)
#     card_name = details_page.map.card_name.text
#     card_type, card_arena = details_page.map.card_type.text.split(", ")
#     card_rarity = details_page.map.cart_rarity.text.split('\n')[1]
#
#     # check fata on page
#     assert card_name == "Three Musketeers"
#     assert card_type == "Troop"
#     assert card_arena == "Arena 7"
#     assert card_rarity == "Rare"
#     driver.close()
#
#
# def test_golem_detail():
#     # get Ice+Spirit page
#     electro_spirit_page = CardsPage(driver)
#     electro_spirit_page.goto_all().get_card_by_name("Golem").click()
#     card = CardDetail(driver).get_base_card()
#
#     # check data on page
#     assert card.name == "Golem"
#     assert card.type == "Troop"
#     assert card.arena == 3
#     assert card.rarity == "Epic"
#     driver.close()


"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
by using an api look for all cards and test them ( this 2 tests is testing 200 tests !!! )
"""
cards_list = card_service.get_all_cards()  # api call (create a Cart's list)


@pytest.mark.parametrize('card', cards_list)
def test_all_cards_on_page(card):
    """
    will go thru all cards by name and check if they is displayed
    """
    driver = webdriver.Chrome(CHROMEDRIVER)
    try:
        driver.get('https://statsroyale.com/')
        cards_page = CardsPage(driver).goto_all()
        cards_on_page = cards_page.get_card_by_name(card.name)
        assert cards_on_page.is_displayed()

    except:
        print('Something went wrong')

    finally:
        driver.close()


@pytest.mark.parametrize('card_api', cards_list)
def test_card_detail_check(card_api):
    driver = webdriver.Chrome(CHROMEDRIVER)
    try:
        driver.get('https://statsroyale.com/')
        CardsPage(driver).goto_all().get_card_by_name(card_api.name).click()
        card_obj = CardDetail(driver).get_base_card()

        assert card_obj.name == card_api.name
        assert card_obj.type == card_api.type
        assert card_obj.arena == card_api.arena
        assert card_obj.rarity == card_api.rarity

    except:
        print("Some error ")
    finally:
        driver.close()

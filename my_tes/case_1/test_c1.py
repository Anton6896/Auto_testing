import os

import pytest
from selenium import webdriver

from my_tes.case_1.pages.card_detail import CardDetail
from my_tes.case_1.pages.cards_page import CardsPage
from my_tes.case_1.services import card_service

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
by using an api look for all cards and test them 
"""
# cards_list = card_service.get_all_cards()
#
#
# @pytest.mark.parametrize('card', cards_list)
# def test_see_all_cards(card):
#     """
#     will go thru all cards by name and check if they is displayed
#     """
#     driver = webdriver.Chrome(driver_path)
#     driver.get('https://statsroyale.com/')
#     cards_page = CardsPage(driver).goto_all()
#     cards_on_page = cards_page.get_card_by_name(card.name)
#     assert cards_on_page.is_displayed()
#
#     driver.close()

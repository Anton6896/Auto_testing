from typing import List

import requests

from my_tes.case_1.models.card import Card


def get_all_cards() -> List[Card]:
    response = requests.get('https://statsroyale.com/api/cards')
    if response.ok:
        return [Card(**card) for card in response.json()]

    else:
        raise Exception(f'Bad response :: code ({response.status_code})')


def get_card_by_name(look_name: str) -> Card:
    cards_list = get_all_cards()
    return next(card for card in cards_list if card.name == look_name)

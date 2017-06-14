from sha.core import card
from sha.dict.card import CARD_TYPE

class sha(card):
    def __init__(self, suit, point):
        card.__init__(self, suit=suit, type=CARD_TYPE['basic'], point=point, name='杀')

class shan(card):
    def __init__(self, suit, point):
        card.__init__(self, suit=suit, type=CARD_TYPE['basic'], point=point, name='闪')

class peach(card):
    def __init__(self, suit, point):
        card.__init__(self, suit=suit, type=CARD_TYPE['basic'], point=point, name='桃')

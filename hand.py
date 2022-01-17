from card import Card
from regular_card import RegularCard
from power_card import SpecialCard


class Hand:
    def __init__(self, received_cards):
        self.hand = received_cards
        self.hand_value = Hand.calculate_hand_value(self.hand)

    @staticmethod
    def calculate_hand_value(hand):
        hand_value = 0
        for card in hand:
            hand_value += card.card_value
        return hand_value
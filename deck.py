from regular_card import RegularCard
from power_card import SpecialCard


class Deck:
    def __init__(self, size):
        super().__init__(size)
        self.size = size
        deck = []

    def generate_deck(self):
        self.card_0_1 = RegularCard.__init__(4,)
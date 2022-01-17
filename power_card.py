from card import Card


class SpecialCard(Card):
    def __init__(self, card_value, amount_in_deck, speciality):
        super().__init__(card_value, amount_in_deck)
        self.speciality = speciality


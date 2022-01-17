class Card:

    def __init__(self, card_value, amount_in_deck):
        self.card_value = card_value
        self.amount_in_deck = amount_in_deck

    def print_card_value(self):
        print(self.card_value)


x = Card(9,4)
x.print_card_value()
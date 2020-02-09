from Card import Card
from Deck import Deck


class Hand:
    cards = []
    point_value_ace_1 = 0
    point_value_ace_11 = 0

    def __init__(self):
        pass

    def __str__(self):
        hand_string = ""
        for card in self.cards:
            hand_string += str(card) + "\n"
        hand_string += f"Points A: {self.point_value_ace_1} \n"
        hand_string += f"Points B: {self.point_value_ace_11} \n"
        return "CARDS IN HAND: \n" + hand_string

    def get_card(self, deck):
        new_card = deck.give_card()
        self.cards.append(new_card)
        self.point_value_ace_1 += new_card.value
        if new_card.figure != 'ace':
            self.point_value_ace_11 += new_card.value
        else:

            self.point_value_ace_11 += 11

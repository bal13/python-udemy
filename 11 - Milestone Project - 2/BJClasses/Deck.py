from Card import Card
import Constants
import random


class Deck:
    cards = []

    def __init__(self):
        for suit in Constants.suit_types:
            for figure in Constants.figure_values:
                card = Card(suit, figure)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += str(card) + "\n"
        return "CARDS IN DECK: \n" + deck_string

    def shuffle(self):
        random.shuffle(self.cards)

    def give_card(self):
        return self.cards.pop()

    def reset(self):
        self.cards  = []
        self.__init__()

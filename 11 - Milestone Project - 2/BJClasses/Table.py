from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from Deck import Deck

class Table:
    pot = 0
    def __init__(self, human_player, computer_player, deck):
        self.human_player = human_player
        self.computer_player = computer_player
        self.deck = deck

    def empty_pot(self):
        # TODO
        pass

    def get_card(self):
        # TODO
        pass
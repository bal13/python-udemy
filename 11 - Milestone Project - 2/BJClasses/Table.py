from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from Deck import Deck


class Table:
    pot = 0

    def __init__(self):
        self.deck = Deck()
        self.human_player = HumanPlayer(self.deck)
        self.computer_player = ComputerPlayer(self.deck)


    def __str__(self):
        table_string = ""
        return f"Player: \n{str(self.human_player)}\nComputer Player: \n{str(self.computer_player)} \nPot: {self.pot}"

    def reset(self):
        self.pot = 0
        self.human_player.reset()
        self.computer_player.reset()
        self.deck.reset()

    def new_round(self):
        self.reset()
        self.human_player.hit(self.deck)
        self.human_player.hit(self.deck)
        self.computer_player.hit(self.deck)
        self.computer_player.hit(self.deck)

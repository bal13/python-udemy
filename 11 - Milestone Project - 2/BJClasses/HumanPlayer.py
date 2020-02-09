from Player import Player
from Hand import Hand


class HumanPlayer(Player):
    balance = 0
    def __init__(self, hand):
        Player.__init__(self, hand)

    def bet(self, bet_ammount):
        # TODO
        pass

    def collect_prize(self, prize_ammount):
        # TODO
        pass
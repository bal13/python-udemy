from Player import Player
from Hand import Hand


class ComputerPlayer(Player):
    def __init__(self, hand):
        Player.__init__(self, hand)
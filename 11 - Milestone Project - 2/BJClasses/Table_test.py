from Deck import Deck
from Hand import Hand
from Player import Player
from Table import Table

deck = Deck()
deck.shuffle()
player = Player(deck)
computer_player = Player(deck)

table = Table(player, computer_player, deck)
table.new_round()
print(table)
table.reset()
print(table)
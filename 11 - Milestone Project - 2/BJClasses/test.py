from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from Table import Table

print("############ Card test cases ###############")
card = Card("spades", "king")
print(card)
print(card.value)
card.show()
print(card)

print("############ Deck test cases ###############")
deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print("Give a card: " + str(deck.give_card()))
print(deck)

print("############ Hand test cases ###############")
hand = Hand()
hand.get_card(deck)
hand.get_card(deck)
hand.get_card(deck)
print(hand)
# print(deck)

print("########### Player test cases #############")
player = Player(hand)
print(player.calculate_score())
print(player)

print("########### Table test cases #############")
computer_hand = Hand()
computer_hand.get_card(deck)
computer_hand.get_card(deck)
computer_hand.get_card(deck)
computer_player = Player(computer_hand)

table = Table(player, computer_player, deck)
print(table)
table.reset()
print(table)
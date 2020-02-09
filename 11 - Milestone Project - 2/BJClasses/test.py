from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player

############ Card test cases ###############
card = Card("spades", "king")
print(card)
print(card.value)
card.show()
print(card)

############ Deck test cases ###############
deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print("Give a card: " + str(deck.give_card()))
print(deck)

############ Hand test cases ###############
hand = Hand()
hand.get_card(deck)
hand.get_card(deck)
hand.get_card(deck)
print(hand)
# print(deck)

########### Player test cases #############
player = Player(hand)
print(player.calculate_score())
print(player)
from Hand import Hand
import Constants


class Player:
    score = 0
    is_bust = False
    is_winner = False

    def __init__(self, deck):
        self.hand = Hand()
        self.deck = deck

    def __str__(self):
        player_string = ""
        return f"PLAYERS HAND: \n{str(self.hand)}\nIs winner: {self.is_winner}\nIs bust: {self.is_bust} "

    def hit(self, deck):
        self.hand.get_card(deck)
        self.calculate_score()

    def stand(self):
        #TODO
        pass

    def calculate_score(self):
        if (self.hand.point_value_ace_1 == Constants.target_score) or \
                (self.hand.point_value_ace_11 == Constants.target_score):
            self.is_winner = True
            return Constants.target_score
        else:
            if self.hand.point_value_ace_1 > Constants.target_score:
                self.is_bust = True
            return self.hand.point_value_ace_1

    def reset(self):
        self.hand = Hand()
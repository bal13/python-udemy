import Constants


class Card:
    value = 0
    is_shown = False

    def __init__(self, suit, figure):
        if suit in Constants.suit_types:
            self.suit = suit
        else:
            raise Exception(f"{suit} is not a valid suit!")
        if figure in Constants.figure_values.keys():
            self.figure = figure
        else:
            raise Exception(f"{figure} is not a valid figure!")

        self.value = Constants.figure_values[figure]

    def __str__(self):
        card_string = "(" + self.suit + " - " + self.figure + ")"
        if self.is_shown:
            return card_string
        else:
            return "HIDDEN CARD - " + card_string

    def show(self):
        self.is_shown = True

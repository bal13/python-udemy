from Table import Table


class Game:
    is_human_turn = True

    def __init__(self):
        self.table = Table()

    def start_round(self):
        self.table.new_round()
        user_input = ''
        while user_input.lower() != "exit":
            print(self.table)
            user_input = input("Mi legyen?\n")
            if user_input.lower() == "hit":
                self.table.human_player.hit(self.table.deck)
            if self.table.human_player.is_bust:
                print("Busteeeed")
                break

    def start_game(self):
        print("Üdv a játékban!")
        play = True
        self.start_round()
        user_input = input("Új kör?\n")
        while play:
            if user_input.lower() == "igen":
                self.start_round()
            else:
                print("Viszlát!")
                play = False

    def turn(self):
        pass

    def switch_sides(self):
        self.is_human_turn = False

    def check_winner(self):
        # TODO
        pass

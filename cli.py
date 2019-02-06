from game_engine.play import Play


class GameEngine:
    """
    This is temporary class for the CLI testing and presentation
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 06/02/2019
    """

    def __init__(self):
        self.play = Play()
        self.introduction()

    def introduction(self):
        print("\n*** Welcome to GameEngine ***")

    def game_mode_selection(self):
        while True:
            print("\nSelect a following game mode (enter number 1 - 3):")
            n = input("1: Player vs Player\n2: Player vs AI\n3: AI vs AI\n")

            if n == "2" or n == "3":
                print("\nSelect a following difficulty (enter number 1 - 3):")
                d = input("1: easy\n2: medium\n3: hard\n")

                if d == "1" or d == "2" or d == "3":
                    self.play.init_players(int(n), int(d))  # initializes play
                    break
            elif n == "1":
                self.play.init_players(int(n))  # initializes the game players
                break


if __name__ == '__main__':
    app = GameEngine()
    app.game_mode_selection()
    app.play.play_turn()

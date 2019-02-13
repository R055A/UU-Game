from game_engine.player_ai import PlayerAI
from random import choice


class PlayerMediumAI(PlayerAI):
    """
    The Medium difficulty AI class
    Author(s):      Gustav From; Adam Ross
    Last-edit-date: 13/02/19
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    @staticmethod
    def get_best(best, dif):
        """
        Selects a preferred piece based on provided difficulty (dif) from a
        provided list of preferred board cells (best). Determines which from
        preference list is best based on the occurrence of the preference. Eg.
        An input list has three cells with equal similarity counts, but one has
        a greater/lesser occurrence of similarities in a combination of
        horizontal, and vertical (and maybe diagonal) rows. Depending on which
        difficulty, the method will return greater (easy) / lesser (hard).
        :param best: list of tuples for preferred moves ((pos), sims, count)
        :param dif: randomly chosen difficulty; hard or easy - True or False
        :return: the selected piece for placing on the board
        """
        sims = [(l, m, n) for l, m, n in list(best.values()) if (dif and m ==
                 min([j for i, j, k in list(best.values())])) or (not dif and m
                 == max([j for i, j, k in list(best.values())]))]  # similarity
        return list(best.keys())[list(best.values()).index(choice([(i, j, k)
                for i, j, k in sims if (dif and k == min([n for l, m, n in
                sims])) or (not dif and k == max([n for l, m, n in sims]))]))]

    def choose_piece(self):
        """
        Method for medium difficulty AI piece choosing. Implements get_best()
        Implements either easy or hard AI algorithms by random 50/50 selection
        :return: the selected piece for placing on the board
        """
        return self.get_best(dict({str(pce): self.easy(self.game.pieces[pce])
                for pce in self.game.pieces}.items()), True) if choice([True,
                False]) else self.get_best(dict({str(pce): self.hard(self.game.
                pieces[pce]) for pce in self.game.pieces}.items()), False)

    def place_piece(self, pce):
        """
        Method for medium difficulty AI piece placing on board
        Implements either easy or hard AI algorithms by random 50/50 selection
        :param pce the piece selected for placing on board
        """
        y, x = self.hard(pce)[0] if choice([True, False]) else self.easy(pce)[0]
        self.game.board[y][x] = pce  # sets the selected piece to a board pos

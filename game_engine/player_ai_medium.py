from game_engine.player_ai import PlayerAI
from random import choice


class PlayerMediumAI(PlayerAI):
    """
    The Medium difficulty AI class
    Author(s):      Gustav From; Adam Ross
    Last-edit-date: 12/02/19
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    @staticmethod
    def select(tpl, dif):
        """
        Searches for and selects a preferred piece based on chosen difficulty
        :param tpl: tuples for every possible move ((pos), similarities, count)
        :param dif: randomly chosen difficulty; hard or easy - True or False
        :return: the selected piece for placing on the board
        """
        sims = [(l, m, n) for l, m, n in list(tpl.values()) if (dif and m ==
                 min([j for i, j, k in list(tpl.values())])) or (not dif and m
                 == max([j for i, j, k in list(tpl.values())]))]
        return list(tpl.keys())[list(tpl.values()).index(choice([(i, j, k) for
                i, j, k in sims if (dif and k == min([n for l, m, n in sims]))
                or (not dif and k == max([n for l, m, n in sims]))]))]

    def choose_piece(self):
        """
        Method for medium difficulty AI piece choosing
        Randomly implements either easy or hard AI algorithms
        :return: the selected piece for placing on the board
        """
        return self.select(dict({str(pce): self.easy(self.game.pieces[pce]) for
                pce in self.game.pieces}.items()), True) if choice([True,
                False]) else self.select(dict({str(pce): self.hard(self.game.
                pieces[pce]) for pce in self.game.pieces}.items()), False)

    def place_piece(self, pce):
        """
        Method for medium difficulty AI piece placing on board
        Randomly implements either easy or hard AI algorithms
        :param pce the piece selected for placing on board
        """
        y, x = self.hard(pce)[0] if choice([True, False]) else self.easy(pce)[0]
        self.game.board[y][x] = pce  # sets the selected piece to a board pos

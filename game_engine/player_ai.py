from game_engine.player_abstract import Player
from random import choice


class PlayerAI(Player):
    """
    AI player abstract class - super class for AI difficulty classes
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 10/02/2019
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    def max_similarities(self, pce):
        """
        Computes the maximum characteristic similarities and the count of the
        maximum similarities across four adjacent board cells in all available
        directions for each available board cell for a given binary piece
        :param pce: potential piece for either selecting or placing on board
        :return: tuples containing ((board position - (y, x)), maximum, count)
        """
        return [(k, max(max([l[m] for m in range(len(l))])), sum([l[m].
                count(max(max([l[m] for m in range(len(l))]))) for m in
                range(len(l))])) for (k, l) in [((i, j), [self.game.bin_count(
                pce, i, j, 0, 1), self.game.bin_count(pce, i, j, 1, 0)] +
                [self.game.bin_count(pce, i, j, 1, 1) if i == j else
                [0, 0, 0, 0]] + [self.game.bin_count(pce, i, j, 1, -1) if i + j
                == 3 else [0, 0, 0, 0]]) for j in range(self.game.N) for i in
                range(self.game.N) if self.is_cell_empty(i, j)]]

    def easy(self, pce):
        """
        Randomly chooses a board cell from computed worst possible next moves
        :param pce: potential piece for either selecting or placing on board
        :return: a tuple containing ((board position), similarities, count)
        """
        print(self.max_similarities(pce))
        return choice(([(i, j, k) for i, j, k in self.max_similarities(pce) if
                       j == 2 or j == min([j for i, j, k in self.
                                          max_similarities(pce)])]))

    def hard(self, pce):
        """
        Randomly chooses a board cell from computed best possible next moves
        :param pce: potential piece for either selecting or placing on board
        :return: a tuple containing ((board position), similarities, count)
        """
        print(self.max_similarities(pce))
        return choice([(m, n, o) for m, n, o in [(i, j, k) for i, j, k in self.
                      max_similarities(pce) if j == max([y for x, y, z in self.
                      max_similarities(pce) if y != 2] + [0])] if o == max([c for a,
                      b, c in self.max_similarities(pce) if b == max([y for x,
                      y, z in self.max_similarities(pce) if y != 2] + [0])] +
                      [0])])

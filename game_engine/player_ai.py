from game_engine.player_abstract import Player
from random import choice


class PlayerAI(Player):
    """
    AI player abstract class - super class for AI difficulty classes
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 12/02/2019
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
        Computes the maximum number of similarities found between each of the
        four characteristics for a given piece across four adjacent board cells
        in each possible horizontal, vertical and diagonal direction for each
        empty board cell and the count of occurrences of this similarity count
        :param pce: potential piece for either selecting or placing on board
        :return: list of tuples: [((pos: y, x), max similarities, count), ...]
        """
        return [(k, max(max([l[m] for m in range(len(l))])), sum([l[m].
                count(max(max([l[m] for m in range(len(l))]))) for m in range
                (len(l))])) for (k, l) in [((i, j), [self.game.bin_count(pce,
                i, j, 0, 1), self.game.bin_count(pce, i, j, 1, 0)] + [self.
                game.bin_count(pce, i, j, 1, 1) if i == j else [0, 0, 0, 0]] +
                [self.game.bin_count(pce, i, j, 1, -1) if i + j == 3 else [0,
                0, 0, 0]]) for j in range(self.game.N) for i in range(self.
                game.N) if self.game.is_cell_empty(i, j)]]

    @staticmethod
    def select_max_similarity_occurrence_count(prfrd_sims, diff):
        """
        Selects randomly from a list of identical best/worst possible moves
        :param prfrd_sims: list of identical best/worst possible next moves
        :param diff: boolean to determine if searching for the min or max count
        :return: a single tuple containing ((pos: y, x), similarities, count)
        """
        return choice([(i, j, k) for i, j, k in prfrd_sims if (diff and k ==
                       max([n for l, m, n in prfrd_sims])) or k == min([n for
                       l, m, n in prfrd_sims])])

    def easy(self, pce):
        """
        Randomly chooses from a list of computed next moves that have either
        the minimum similarity of all potential next moves or a similarity of
        two and the greatest occurrence count of the selected similarity count
        For the first four plays a purely random board position is returned
        :param pce: potential piece for either selecting or placing on board
        :return: a single tuple containing ((pos: y, x), similarities, count)
        """
        sims = self.max_similarities(pce)  # max similarities & their counts
        return self.select_max_similarity_occurrence_count([(i, j, k) for i, j,
                k in sims if (j == 2 and 2 in [m for l, m, n in sims]) or j ==
                min([m for l, m, n in sims])] if len(self.game.pieces) < 13
                else [choice([((y, x), 1, 1) for x in range(self.game.N) for y
                in range(self.game.N) if self.game.is_cell_empty(y, x)])], 0)

    def hard(self, pce):
        """
        Randomly chooses from a list of computed next moves that have either
        the maximum similarity of all potential next moves if that similarity
        is not two and the greatest occurrence count of that similarity count
        For the first two plays a purely random board position is returned
        :param pce: potential piece for either selecting or placing on board
        :return: a single tuple containing ((pos: y, x), similarities, count)
        """
        sims = self.max_similarities(pce)  # max similarities & their counts
        return self.select_max_similarity_occurrence_count([(i, j, k) for i, j,
                k in sims if (len([m for l, m, n in sims if m != 2]) > 0 and j
                == max([m for l, m, n in sims if m != 2])) or j == max([m for
                l, m, n in sims])] if len(self.game.pieces) < 15 else [choice([
                ((y, x), 0, 0) for x in range(self.game.N) for y in range(self.
                game.N) if self.game.is_cell_empty(y, x)])], 1)

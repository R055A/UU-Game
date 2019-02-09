from game_engine.node import Node
import math


class Minimax:
    """
    The Minimax algorithm for evaluating different moves
    """

    def __init__(self, board_state, depth):
        self.board_state = board_state
        self.depth = depth
        self.root_nodes = []
        self.build_evaluation_trees()
        self.minimax(0, 0, 0, 0, True)

    def build_evaluation_trees(self):
        remaining_spots = self.board_state.get_remaining_spots()
        remaining_pieces = self.board_state.get_remaining_pieces()
        root_num = 0
        for i in len(remaining_spots):
            for j in len(remaining_pieces):
                self.root_nodes[root_num] = self.build_evaluation_tree(remaining_spots[i], remaining_pieces[j], self.board_state)
                root_num += 1

    def build_evaluation_tree(self, board_state):
        node = Node()
        new_board_state = board_state.copy()
        remaining_spots = new_board_state.get_remaining_spots()
        remaining_pieces = new_board_state.get_remaining_pieces()
        for i in len(remaining_spots):
            if len(remaining_pieces):
                for j in len(remaining_pieces):
                    node.add_child(self.build_evaluation_tree())
            else:
                node.add_child(self.build_evaluation_tree())
        return node

    def minimax(self, node, depth, alpha, beta, maximize):
        if depth == 0:
            if node.has_won_game():
                return 1 if node.is_my_turn() else -1
            else:
                return 0

        if maximize:
            max_eval = -math.inf
            for child in node.get_children():
                eval = self.minimax(self, child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha.eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for child in node.get_children:
                eval = self.minimax(self, child, depth - 1, alpha, beta, True)
                min_eval = max(min_eval, eval)
                alpha = max(alpha.eval)
                if beta <= alpha:
                    break
            return min_eval

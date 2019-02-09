from game_engine.node import Node
import math


class Minimax:
    """
    The Minimax algorithm for evaluating different moves
    """

    def __init__(self, game, depth):
        """
        ...
        :param game: ...
        :param depth: ...
        """
        self.game = game
        self.depth = depth
        self.root_nodes = []

    def get_move(self):
        """
        ...
        """
        remaining_spots = self.game.get_remaining_spots()
        remaining_pieces = self.game.get_remaining_pieces()
        root_num = 0
        for i in range(len(remaining_spots)):
            for j in range(len(remaining_pieces)):
                self.root_nodes[root_num] = self.build_evaluation_tree(remaining_spots[i], remaining_pieces[j],
                                                                       self.game, self.depth)
                root_num += 1

        best_move = 0
        for root in self.root_nodes:
            root = self.minimax(root, self.depth, -math.inf, math.inf, True)
            if root > best_move:
                best_move = root

    def build_evaluation_tree(self, piece, cell, next_piece, player, board_state, depth):
        """
        ...
        :param piece: ...
        :param cell: ...
        :param next_piece: ...
        :param player: ...
        :param board_state: ...
        :param depth: ...
        """
        node = Node()
        new_board_state = board_state.copy()

        if depth == 0:
            node.is_leaf = True
            return node

        remaining_spots = new_board_state.get_remaining_spots()
        remaining_pieces = new_board_state.get_remaining_pieces()
        for i in range(len(remaining_spots)):
            if len(remaining_pieces) > 0:
                for j in range(len(remaining_pieces)):
                    node.add_child(
                        self.build_evaluation_tree(next_piece, remaining_spots[i], remaining_pieces[j], new_board_state,
                                                   depth - 1))
            else:
                node.add_child(
                    self.build_evaluation_tree(next_piece, remaining_spots[i], 16, new_board_state, depth - 1))
        return node

    def minimax(self, node, alpha, beta, maximize):
        """
        ...
        :param node: ...
        :param depth: ...
        :param alpha: ...
        :param beta: ...
        :param maximize: ...
        """
        if node.is_leaf():
            if node.has_won_game():
                return 1 if node.is_my_turn() else -1
            else:
                return 0

        if maximize:
            max_eval = -math.inf
            for child in node.get_children():
                eval = self.minimax(child, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for child in node.get_children:
                eval = self.minimax(child, alpha, beta, True)
                min_eval = min(min_eval, eval)
                alpha = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def print_tree(self, node):
        """
        ...
        :param node: ...
        """
        print(node.print_node())
        child_string = ""
        for child in node.get_children():
            child_string += child.get_string()
        print(child_string)
        for child in node.get_children():
            self.print_tree(child)

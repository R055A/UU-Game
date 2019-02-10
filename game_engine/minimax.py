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

    def get_move(self):
        """
        ...
        """
        remaining_spots = self.game.get_remaining_spots()
        remaining_pieces = self.game.get_remaining_pieces()
        passed_piece = self.game.get_passed_piece()
        root_nodes = []

        for i in range(len(remaining_spots)):
            for j in range(len(remaining_pieces)):
                root_nodes.append(
                    self.build_evaluation_tree(passed_piece, remaining_spots[i], remaining_pieces[j], True, self.game,
                                               self.depth))

        best_move = 0

        for root in root_nodes:
            current_move = self.minimax(root, -math.inf, math.inf)
            if current_move > best_move:
                best_move = root
        return root_nodes[best_move]

    def build_evaluation_tree(self, passed_piece, cell, next_piece, is_my_turn, game, depth):
        """
        ...
        :param passed_piece: ...
        :param cell: ...
        :param next_piece: ...
        :param is_my_turn: ...
        :param game: ...
        :param depth: ...
        """
        node = Node(is_my_turn, passed_piece, cell)
        new_board_state = game.clone_game()
        new_board_state.place_piece(cell, passed_piece)

        if new_board_state.has_won_game():
            node.set_is_leaf()
            node.set_has_won()
            return node

        if depth == 0 or next_piece == 16:
            node.set_is_leaf()
            return node

        if is_my_turn:
            is_my_turn = False
        else:
            is_my_turn = True

        new_board_state.pass_piece(next_piece)
        remaining_spots = new_board_state.get_remaining_spots()
        remaining_pieces = new_board_state.get_remaining_pieces()
        for i in range(len(remaining_spots)):
            if len(remaining_pieces) > 0:
                for j in range(len(remaining_pieces)):
                    node.add_child(
                        self.build_evaluation_tree(next_piece, remaining_spots[i], remaining_pieces[j], is_my_turn,
                                                   new_board_state,
                                                   depth - 1))
            else:
                node.add_child(
                    self.build_evaluation_tree(next_piece, remaining_spots[i], 16, is_my_turn, new_board_state, depth - 1))
        return node

    def minimax(self, node, alpha, beta):
        """
        ...
        :param node: ...
        :param depth: ...
        :param alpha: ...
        :param beta: ...
        :param maximize: ...
        """
        if node.is_leaf():
            if node.has_won():
                return 1 if node.is_my_turn() else -1
            else:
                return 0

        if node.is_my_turn():
            max_eval = -math.inf
            for child in node.get_children():
                eval = self.minimax(child, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for child in node.get_children:
                eval = self.minimax(child, alpha, beta)
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

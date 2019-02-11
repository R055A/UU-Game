from game_engine.node import Node
import math


class Minimax:
    """
    The Minimax algorithm for evaluating different moves
    Author(s): Viktor Enzell
    Last-edit-date: 10/02/2019
    """

    def __init__(self, game, depth, passed_piece):
        """
        Initialises the class variables
        :param game: the game instance
        :param depth: the depth where the algorithm should stop its search
        """
        self.board_state = game
        self.depth = depth
        self.passed_piece = passed_piece

    def get_move(self):
        """
        Builds an evaluation tree for each possible move
        based on the current state of the game and the passed piece
        :return: the root node of the evaluation tree with the highest cost
        """
        remaining_spots = self.board_state.get_remaining_spots()
        remaining_pieces = self.board_state.get_remaining_pieces()
        root_nodes = []

        for i in range(len(remaining_spots)):
            for j in range(len(remaining_pieces)):
                root_nodes.append(
                    self.build_evaluation_tree(self.passed_piece,
                                               remaining_spots[i],
                                               remaining_pieces[j],
                                               True,
                                               self.board_state,
                                               self.depth))

        best_move = 0

        for root in root_nodes:
            current_move = self.minimax(root, -math.inf, math.inf)
            if current_move > best_move:
                best_move = root
        return root_nodes[best_move]

    def build_evaluation_tree(self, passed_piece, spot, next_piece, is_my_turn, board_state, depth):
        """
        Recursively builds a tree of possible moves.
        Each call makes a node from the previously passed piece and spot
        and adds as children to the node every other possible move
        :param passed_piece: the piece chosen by the opponent
        :param spot: the spot of the board where to place the passed piece
        :param next_piece: the piece to be passed to child node
        :param is_my_turn: true at root node, false at child of root, true at child of child of root and so on
        :param board_state: the current game instance
        :param depth: the depth of the node
        :return: the root node of the tree
        """
        node = Node(is_my_turn, passed_piece, spot)
        new_board_state = board_state.clone_game()
        new_board_state.place_piece(spot, passed_piece)

        if new_board_state.has_won_game():
            node.set_is_leaf()
            node.set_has_won()
            return node

        if depth == 0 or next_piece == 16:
            node.set_is_leaf()
            return node

        new_board_state.pass_piece(next_piece)
        remaining_spots = new_board_state.get_remaining_spots()
        remaining_pieces = new_board_state.get_remaining_pieces()
        for i in range(len(remaining_spots)):
            if len(remaining_pieces) > 0:
                for j in range(len(remaining_pieces)):
                    node.add_child(
                        self.build_evaluation_tree(next_piece,
                                                   remaining_spots[i],
                                                   remaining_pieces[j],
                                                   not is_my_turn,
                                                   new_board_state,
                                                   depth - 1))
            else:
                node.add_child(
                    self.build_evaluation_tree(next_piece,
                                               remaining_spots[i],
                                               16,
                                               not is_my_turn,
                                               new_board_state,
                                               depth - 1))
        return node

    def minimax(self, node, alpha, beta):
        """
        Minimax algorithm with alpha beta pruning.
        The method is recursively called for the children of node
        and the leaves are evaluated.
        :param node: the node to evaluate
        :param alpha: -infinity if no pruning occurs otherwise the cost of the most likely move
        :param beta: infinity if no pruning occurs otherwise the cost of the most likely move
        :return: the cost of the tree
        """
        if node.is_leaf:
            if node.has_won:
                return 1 if node.is_my_turn else -1
            else:
                return 0

        if node.is_my_turn:
            max_eval = -math.inf
            for child in node.children:
                eval = self.minimax(child, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for child in node.children:
                eval = self.minimax(child, alpha, beta)
                min_eval = min(min_eval, eval)
                alpha = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def print_tree(self, node):
        """
        Recursively prints tree
        :param node: root node
        """
        print(node.get_string())
        child_string = ""
        for child in node.children:
            child_string += child.get_string()
        print(child_string)
        for child in node.children:
            self.print_tree(child)

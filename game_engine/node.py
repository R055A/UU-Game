class Node:
    """
    A node in the evaluation tree
    """

    def __init__(self, is_my_turn, passed_piece, cell):
        """
        Initialises the class variables
        :param ...: ...
        """
        self.cell = cell
        self.passed_piece = passed_piece
        self.is_my_turn = is_my_turn
        self.children = []
        self.is_leaf = False
        self.has_won = False

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_string(self):
        return "My turn: " + str(self.is_my_turn) + "'s turn. Leaf: " + str(self.is_leaf)

    def is_leaf(self):
        return self.is_leaf

    def set_is_leaf(self):
        self.is_leaf = True

    def is_my_turn(self):
        return self.is_my_turn

    def set_has_won(self):
        self.has_won = True

    def has_won(self):
        return self.has_won

    def get_cell(self):
        return self.cell

    def get_passed_piece(self):
        return self.passed_piece

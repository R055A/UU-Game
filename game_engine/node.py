class Node:
    """
    A node in the evaluation tree
    """

    def __init__(self, player):
        """
        Initialises the class variables
        :param ...: ...
        """
        self.player = player
        self.children = []
        self.is_leaf = False

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_string(self):
        return "Player " + str(self.player) + "'s turn. Leaf: " + str(self.is_leaf)

    def is_leaf(self):
        return self.is_leaf

class Node:
    """
    A node in the evaluation tree
    """

    def __init__(self):
        """
        Initialises the class variables
        :param ...: ...
        """
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

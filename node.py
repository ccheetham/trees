class Node(object):

    def __init__(self, name):
        """
        :param name: str
        """
        self.name = name
        self.children = []

    def add_child(self, node):
        """

        :param node:
        """
        self.children.append(node)

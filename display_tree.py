import sys

from node import Node

NEWLINE = '\n'
INDENT = '    '


def display_tree(node, indent='', out=sys.stdout):
    """
    Each node name is printed on its own line.

    For each level of the tree, an indent is added.
    The indent of a level is: (level - 1) * indent.
    An item on level 1 would have no indent.
    An item on level 3 would have 2 indents.


    :param Node node:
    :param str indent:
    :param io.TextIOBase out:
    """
    pass

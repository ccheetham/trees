from io import StringIO

from display_tree import display_tree
from node import Node

NEWLINE = '\n'
INDENT = '    '


def test_single_node():
    tree = Node("unicorn")
    out = StringIO()
    display_tree(tree, out=out)
    assert out.getvalue() == f"unicorn{NEWLINE}"


def test_traversal():
    top = Node("top")
    left = Node("left")
    right = Node("right")
    bottom = Node("bottom")

    top.add_child(left)
    top.add_child(right)
    left.add_child(bottom)
    out = StringIO()
    display_tree(top, out=out)
    assert out.getvalue() == f"top{NEWLINE}{INDENT}left{NEWLINE}{INDENT}{INDENT}bottom{NEWLINE}{INDENT}right{NEWLINE}"

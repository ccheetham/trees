from node import Node
from display_tree import display_tree

if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")
    i = Node("i")
    a.add_child(b)
    a.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(g)
    c.add_child(i)
    e.add_child(f)
    g.add_child(h)
    display_tree(a)

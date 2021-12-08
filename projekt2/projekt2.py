from typing import Any, Callable
from lab5 import BinaryNode, BinaryTree

def left_line(tree: BinaryTree):
    child = tree.root
    list = [child]
    while child != None:
        if child.left_child != None:
            list.append(child.left_child)
        child = child.left_child
    return list

# tree2 = BinaryTree(10)
# tree2.root.add_left_child(9)
# tree2.root.left_child.add_left_child(1)
# tree2.root.left_child.add_right_child(3)
# tree2.root.add_right_child(2)
# tree2.root.right_child.add_left_child(4)
# tree2.root.right_child.add_right_child(6)
#
# lista_tree2 = left_line(tree2)
# for i in lista_tree2:
#     print(i.value)

tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.left_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
tree.root.right_child.add_right_child(7)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)
tree.show()

lista_tree = left_line(tree)
for i in lista_tree:
    print(i.value)
from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value):
        self.left_child = None
        self.right_child = None
        self.value = value

    def is_leaf(self):
        if self.left_child == None and self.right_child == None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order()
        if self.right_child != None:
            self.right_child.traverse_pre_order()

    def __str__(self):
        return str(self.value)

    def show(self, temp=0):
        if self != None:
            if self.right_child != None:
                self.right_child.show(temp + 1)
            if self.left_child != None and self.right_child != None:
                print(' '* 6 * temp, self.value, '->')
            else:
                print(' '* 6 * temp, self.value)
            if self.left_child != None:
                self.left_child.show(temp + 1)

# node = BinaryNode(1)
# node.add_left_child(2)
# node.add_right_child(3)
# node.left_child.add_left_child(4)
# node.left_child.add_right_child(5)
# node.right_child.add_left_child(6)
# node.right_child.add_right_child(7)
#
# print(node)
# print(f'{node.left_child} {node.right_child}')
# print(f'{node.left_child.left_child} {node.left_child.right_child} '
#       f'{node.right_child.left_child} {node.right_child.right_child}')
#
# node.show()

class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_orderd(self):
        self.root.traverse_in_order()

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order()

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order()

    def show(self):
        self.root.show()
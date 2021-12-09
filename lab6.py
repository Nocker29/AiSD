from typing import Any

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self):
        if self.left_child.value < self.right_child.value:
            return self.left_child
        return self.right_child

class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def insert(self, value: Any) -> None:

        return 1

    def _insert(self, node: BinaryNode, value: Any):

        return node

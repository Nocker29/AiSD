from typing import Any, List, Callable
from lab2 import Queue

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value, child: List['TreeNode'] = []):
        self.value=value
        self.children = child.copy()
        self.parent=None

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.children==[]:
            return True
        return False

    def add(self,child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        if self.children != []:
            for child in self.children:
                child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        _queue = Queue()
        for child in self.children:
            _queue.enqueue(child)
        while len(_queue) != 0:
            node = _queue.dequeue()
            visit(node)
            for i in node.children:
                _queue.enqueue(i)

    def search(self, value:Any):
        if self.value==value:
            return True
        for child in self.children:
            if child.search(value):
                return True
        return False

class Tree:
    root: TreeNode

    def __init__(self, child:'TreeNode'):
        self.root = child
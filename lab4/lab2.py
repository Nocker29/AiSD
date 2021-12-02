from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        if (self.next == None):
            return f'{self.value}'
        return f'{self.value} -> {self.next}'

class LinkedList:
    head = Node
    tail = Node
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value:Any) -> None:
        dane=Node(value)
        if (self.tail!=None):
            self.tail.next=dane
        self.tail=dane
        if (self.head == None):
            self.head = dane

    def push(self,value:Any) -> None:
        dane=Node(value)
        dane.next=self.head
        self.head=dane
        if(self.tail==None):
            self.tail=dane

    def __len__(self):
        len=0
        dane=self.head
        while(dane!=None):
            dane=dane.next
            len+=1
        return len

    def node(self,at:int) -> Node:
        if(at<len(self)):
            dane=self.head
            for at in range(at):
                dane=dane.next
            return dane
        return None

    def insert(self, value: Any, after: Node) -> None:
        dane=Node(value)
        dane.next=after.next
        after.next=dane

    def pop(self) -> Any:
        dane=self.head
        self.head=dane.next
        return dane.value

    def remove_last(self) -> Any:
        dane=self.tail
        ostatnie=self.head
        while(ostatnie.next.next!=None):
            ostatnie=ostatnie.next
        ostatnie.next=None
        self.tail=ostatnie
        return dane.value

    def remove(self, after: Node) -> Any:
        after.next=after.next.next

    def __str__(self):
        return f'{self.head}'

class Stack:
    _storage=LinkedList()

    def __len__(self):
        len = 0
        dane = self._storage.head
        while (dane != None):
            dane = dane.next
            len += 1
        return len

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()

    def __str__(self):
        if stack._storage.head == None:
            return str(self._storage.head)
        nastepne = self._storage.head.next
        dane = str(self._storage.head.value)
        while nastepne != None:
           dane += '\n' + str(nastepne.value)
           nastepne = nastepne.next
        return dane

class Queue:
    _storage=LinkedList()

    def __len__(self):
        return len(self._storage)

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self):
        if self._storage.head==None:
            return str(self._storage.head)
        dane=str(self._storage.head.value)
        nastepna=self._storage.head.next
        while nastepna!=None:
            dane+=', '+str(nastepna.value)
            nastepna=nastepna.next
        return dane

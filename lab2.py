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

print("\nZAD 1 ----------------------------------------")

list_=LinkedList()
assert list_.head==None

list_.push(1)
list_.push(0)
print(list_)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)
print(list_)
assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
print(list_)

first_element = list_.node(at=0)
returned_first_element = list_.pop()
print(first_element.value)
print(returned_first_element)
assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
print(last_element)
print(returned_last_element)
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)
print(list_)
assert str(list_) == '1 -> 5'

print("\nZAD 2 ----------------------------------------")

stack=Stack()

print(f'{stack}\n-------')
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print(f'{stack}\n-------')

top_value = stack.pop()
assert top_value == 1
print(stack)

assert len(stack) == 2

print("\nZAD 3 ----------------------------------------")

queue = Queue()
print(queue)

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue)
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
print(queue)
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
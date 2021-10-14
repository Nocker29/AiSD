# a: str = 'abc'
# print(a)
# print(type(a))
#
# class House:
#     doors: int
#     color: str
#
#     def __init__(self, doors: int, color: str) -> None:
#         self.doors=doors
#         self.color=color
#
#     def change_color(self, new_color: str) -> None:
#         if new_color == self.color:
#             print('Operacja jest niedozwolona')
#             return
#         self.color = new_color
#
#     def __str__(self) -> str:
#         return f'liczba drzwi: {self.doors}, kolor elewacji: {self.color}'
#
# green_house: House = House(doors=30, color='green')
# print(green_house.doors)
# print(green_house.color)
# print(green_house)

# assert 1 == 12
# def sum_(x:int, y:int) ->int:
#     return x+y
# assert sum_(2,2) == 4
# assert sum_(4,6) == 10

from typing import Any

#zad1
class Node:
    value: Any
    next: 'Node'

class LinkedList:
    head: Node
    tail: Node


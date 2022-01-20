from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    i = 0
    n = len(numbers)
    while (i <= n):
        middle = int((i + len(numbers)) / 2)
        if (numbers[middle] == value):
            return True, middle
        elif (numbers[middle] < value):
            n += 1
        else:
            i -= 1
    return False, -1  # wartosc nie zostala znaleziona


ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])

result = binary_search(ints, 7)
print(result)
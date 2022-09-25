"""
- randomizes order of list repeatedly until it is sorted

bad algorithm
worst sorting algorithm
"""


import random 
import sys

numbers = [5,8,1,4,7]

# check if the list is sorted
def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index +1 ]:
            return False
    return True


def bogo_sort(values):
    while not is_sorted(values):
        random.shuffle(values)
    return values

print(bogo_sort(numbers))

from collections import deque

# create an empty deque 
deque()

# use different iterables to create deques  -deque([])
print(deque((1,2,3,4)))

# deque([1, 2, 3, 4]) 
print(deque([1,2,3,4]))

# deque([1, 2, 3, 4]) 
deque(range(1,5))

# deque(['a', 'b', 'c', 'd']) 
print(deque("abcd"))

numbers = {"one":1,"two":2,"three":3,"four":4}

# deque(['one', 'two', 'three', 'four']) 
print(deque(numbers.keys()))

# deque([1, 2, 3, 4]) 
print(deque(numbers.values()))

# deque([('one', 1), ('two', 2), ('three', 3), ('four', 4)]) 
print(deque(numbers.items()))


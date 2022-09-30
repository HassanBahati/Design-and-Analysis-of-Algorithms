from collections import deque
stack = deque()

stack.append('7')
stack.append('6')
stack.append('5')

print(stack)

# deque(['a', 'b', 'c'])

stack.pop()

print(stack)
from collections import deque
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)

# deque(['a', 'b', 'c'])

myStack.pop()
print(myStack)
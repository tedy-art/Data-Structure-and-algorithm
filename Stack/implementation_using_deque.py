from collections import deque
stack = deque()
stack.append("x")
print(stack)
stack.append("y")
stack.append("z")
print(stack)
print(stack.pop())
print(stack)
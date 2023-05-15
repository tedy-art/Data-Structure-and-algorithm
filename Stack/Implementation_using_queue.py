# Implementation using queue
from queue import LifoQueue

# assign LifoQueue() function to stack variable
stack = LifoQueue(maxsize = 3) # maxsize of stack is 3
stack.put(2) # insert 1st element
stack.put(3) # insert 2st element
stack.put(4) # insert 3st element
print(stack.qsize()) # size of stack
print(stack.full()) # True (stack is full)
print(stack.get()) # remove
print(stack.full()) # false (stack is not full)
class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

        # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[0]

Astack = Stack()
Astack.add("mon")
Astack.add("Tue")
Astack.peek()
print(Astack.peek())
Astack.add("wed")
Astack.add("The")
print(Astack.peek())
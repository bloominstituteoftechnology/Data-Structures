"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   - Using a list means that either enqueuing or dequeuing a value is O(n)
   - Using a a LinkedList means that both are O(1)
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from stack.stack import Stack


class Queue:
    def __init__(self):
        self.incoming = Stack()
        self.outgoing = Stack()

    def __len__(self):
        return len(self.incoming) + len(self.outgoing)

    def enqueue(self, value):
        self.incoming.push(value)

    def dequeue(self):
        if len(self) > 0:
            if len(self.outgoing) == 0:
                while len(self.incoming) > 0:
                    self.outgoing.push(self.incoming.pop())
            return self.outgoing.pop()
        else:
            return None

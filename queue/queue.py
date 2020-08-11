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
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        len(self.storage)

    def is_empty(self):
        return len(self.storage) == 0

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.is_empty():
            return ('Queue is empty!')
        return self.storage.pop(0)

    def first(self):
        if self.is_empty():
            return ('Queue is empty!')
        return self.storage[0]


q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(q.storage)
q.dequeue()
q.dequeue()
print(q.storage)

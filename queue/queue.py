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
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        self.storage.pop(0)
        self.size -= 1

    def view(self):
        return self.storage

class Queues:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList(None,None)
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        self.storage.remove_tail()

    def view(self):
        return self.storage.view()

que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que.view())
que.dequeue()
print(que.view())

# Linked list implementation 
que = Queues()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que.view())
que.dequeue()
print(que.view())
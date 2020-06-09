"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 
***Monday assignment***(Mandi inserted)
FIFO (first in first out): lookup O(n), enqueue O(1), dequeue O(1), peek O(1)
                1       2     3        4 (for arrays)
                head                   tails (for linked lists)
ex: wait list: Matt-- Joy -- Samir --Pavel
can use arrays or linked lists to create --> SHOULD implelement them with linked lists though


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
        self.storage = LinkedList()

    def __len__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

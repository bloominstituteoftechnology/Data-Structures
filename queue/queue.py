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

from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # I used DLL because it is efficient runtime.
        self.storage = DoublyLinkedList()
    

    # Here it will return number of items in queue
    def __len__(self):
        return self.size

    #adding an item to the back of th queu
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    #remving and return an item from the front of the queue
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None
        

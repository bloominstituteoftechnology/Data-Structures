import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

"""
Follows FIFO(first in first out protocol) with enqueue(), dequeue() and peek() methods
gives you the option of creating bounded queues with a max_size. 
prevents queue "overflow" and "underflow" by keeping track of size. 
"""

class Queue:
    def __init__(self, max_size=None):  # Allows for bounded queues.
        self.size = 0
        self.max_size = max_size
        self.storage = LinkedList()
        self.head = None
        self.tail = None

    def enqueue(self, item):
        if self.has_space():
            if self.is_empty():
                # the item is the head and the tail.
                self.head = item
                self.tail = item
            else:
                self.tail = item
                # also need to self.tail.set_next_node(item)
            self.size += 1
            self.storage.append(item)
        else:
            print("The queue has no more room!")

    def dequeue(self):
        if self.len() > 0:
            item_to_remove = self.head
            if self.len() == 1:
                # then this pop will set the list to zero
                # head and tail must now equal none
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
            popped = self.storage.pop()
            self.size -= 1
            return item_to_remove.get_value()

        else:
            print("This queue is totally empty!")

    def len(self):
        return self.size

    def peek(self):
        # return self.head.get_value()
        """Peek at the head without removing it. """
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.head.get_value()

    def has_space(self):
      # prevents queue overflow
        """  it allows us to see if we can enqueue() a new value on the end of the queue.  """
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.len()

    def is_empty(self):
        return self.size == 0
        # this is neccessary because you cannot remove from a
        # empty list or you get queue underflow

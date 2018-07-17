import sys

sys.path.append("../linked_list")
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        # increase the size of the queue by one
        self.size += 1
        # invoke "add_to_tail" on self.storage, passing in (item) as an argument
        self.storage.add_to_tail(item)

    def dequeue(self):
        # if the size of the queue is greater than one, decrement the size
        if self.size > 0:
            self.size -= 1
            # invoke "remove_head" on self.storage
            return self.storage.remove_head()
        else:
            # if the size of the queue is less than or equal to zero, return None
            return None

    def len(self):
        # return the size of the queue
        return self.size

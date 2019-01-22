import sys
sys.path.append('../linked_list')
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)

    def dequeue(self):
        self.storage.remove_head()
        if self.storage.head is None:
            return None
        if self.storage.head.value:
            return self.storage.head.value - 1



    def len(self):
        return self.size

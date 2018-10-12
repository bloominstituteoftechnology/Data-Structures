import sys
sys.path.append('../linked_list')
from linked_list import LinkedList  # noqa


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        removed = self.storage.remove_head()
        if removed is not None:
            self.size -= 1
        return removed

    def len(self):
        return self.size

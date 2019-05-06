
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

     # item should be added to the back

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    # item should be removed from front of queue
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            return self.storage.remove_head()

    def len(self):
        return self.size

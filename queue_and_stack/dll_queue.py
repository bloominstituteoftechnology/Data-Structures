import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # Adds item/node to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # Deletes item/node from the front of the queue
    def dequeue(self):
        # if there are no items in queue
        if not self.storage.head and not self.storage.tail:
            return
        else:
            # remove the last item from the queue
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

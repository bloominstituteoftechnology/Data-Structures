import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList(self)

    # Adds item/node to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    # Deletes item/node from the front of the queue
    def dequeue(self):
        # if there is only one item remove and return
        if not self.storage.head and not self.storage.tail:
            return

        # if there is only one item in queue remove it.
        if self.storage.head is self.storage.tail:
            self.storage.tail = None
            return

        # remove the last item from the queue
        self.storage.tail = self.storage.tail.prev
        self.size -= 1

        return self.storage.tail.value

    def len(self):
        return self.size

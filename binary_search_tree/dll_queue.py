

from doubly_linked_list import DoublyLinkedList
import sys


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #     because we will only ever need to enqueue or dequeue from the tail or head of the list
        #     and we already have functions created to help us do this
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        result = self.storage.add_to_tail(value)
        self.size = self.storage.length
        return result

    def dequeue(self):
        if self.size > 0:
            result = self.storage.remove_from_head()
            self.size = self.storage.length
            return result
        else:
            return None

    def len(self):
        return self.storage.length

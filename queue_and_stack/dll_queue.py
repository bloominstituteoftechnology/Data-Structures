import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = {}

    def enqueue(self, value):
        DoublyLinkedList.add_to_tail(value)

    def dequeue(self):
        if self.head:
            self.head = self.head.next()
            DoublyLinkedList.delete(self)
        else:
            DoublyLinkedList.delete(self)
    def len(self):
        return self.length

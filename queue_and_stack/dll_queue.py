import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # you need to keep popping things off the head and have a new head
        # you also need to add to the tail without changing the head
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            value = self.storage.head.value
            self.storage.remove_from_head()
            self.size -= 1
            return value
        else:
            print("the queue is empty")

    def len(self):
        return self.size
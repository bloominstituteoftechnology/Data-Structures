# from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Pretty straight-forward to add to head & tail, and remove from head & tail.
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add to tail
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # Remove head
        value = self.storage.remove_from_head()
        if self.len() > 0:
            self.size -= 1
        return value

    def len(self):
        return self.size

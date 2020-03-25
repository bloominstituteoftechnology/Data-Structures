import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It is a very efficient structure to implement stacks. with a O(n) complexity.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head.value
        self.size += 1

    def dequeue(self):
        # Check that there is something in the queue to remove
        if self.size == 0:
            print("The stack is empty")
            return
        else:
            self.storage.remove_from_tail()
            self.size -= 1

    def len(self):
        return self.size
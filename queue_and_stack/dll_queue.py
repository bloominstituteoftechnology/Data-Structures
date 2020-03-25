import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It is a very efficient structure to implement queues with a O(n) complexity.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail.value
        self.size += 1


    def dequeue(self):
        # Check that there is something in the queue to remove
         if self.size == 0:
            print("The queue is empty")
            return
        value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1


    def len(self):
        return self.size
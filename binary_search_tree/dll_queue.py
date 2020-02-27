from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? Because the length isn't predefined ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value): #should add an item to the back of the queue.
        self.storage.add_to_tail(value)
        self.size = self.storage.length

    def dequeue(self): #should remove and return an item from the front of the queue.
        value = None
        if self.size > 0:
            value = self.storage.remove_from_head()
            self.size = self.storage.length
        return value

    def len(self): #returns the number of items in the queue.
        self.size = self.storage.length
        return self.size

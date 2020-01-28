import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        
            # It can be traversed in both forward and backward direction, as well as the delete operation is more efficent if the pointer to the node to be deleted is given.

        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        # pass

    def dequeue(self):
        return self.storage.remove_from_head()
        # pass

    def len(self):
        return self.storage.__len__()
        # pass

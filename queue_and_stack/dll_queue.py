
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? because it is efficient runtime
        self.storage = DoublyLinkedList()

        #adding an item to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1


        #removing and return and item from the front of the queue
    def dequeue(self):
        if self.size > 0:
            self.size -=1
            return self.storage.remove_from_head()
        else:
            return None


        #return number of items in queue
    def len(self):
        return self.size

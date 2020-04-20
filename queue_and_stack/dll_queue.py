import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue(DoublyLinkedList):
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #add to size
        self.size += 1
        # if head and tail are None, set to vaLue
        if self.storage.head == None:
            self.storage.add_to_head(value)
        else:
            self.storage.add_to_tail(value)


    def dequeue(self):
        if self.size == 0:
            return None;

        #take from size
        self.size -=1
        #store value of head
        tor = self.storage.head.value
        #use built-in function to remove it from queue
        self.storage.remove_from_head()
        return tor


    def len(self):
            return self.size

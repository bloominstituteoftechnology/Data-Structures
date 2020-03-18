import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def __str__(self):
        return print(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
       return self.storage.remove_from_head()


    def len(self):
       return self.storage.length


#
# q = Queue()
# q.enqueue(100)
# q.enqueue(101)
# q.enqueue(105)
# print(q.dequeue())
#
# print(q)


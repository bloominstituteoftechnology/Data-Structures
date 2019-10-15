import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#FIFO
'''
1. Should have the methods: enqueue, dequeue, and len.
2. enqueue should add an item to the back of the queue.
3. dequeue should remove and return an item from the front of the queue.
4. len returns the number of items in the queue.
'''
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        self.storage.remove_from_tail()
        self.size -= 1
        return self

    def len(self):
        return self.size


queue = Queue()
queue.enqueue("hi")
queue.enqueue("hello")
queue.enqueue("yo")
queue.dequeue()
print(f'length: {queue.len()}')

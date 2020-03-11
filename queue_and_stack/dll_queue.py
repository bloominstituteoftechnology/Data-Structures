
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?c
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(ListNode(value))

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            self.storage.remove_from_head()

    def len(self):
        return self.storage.length


my_queue = Queue()
print(my_queue)
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(6)
my_queue.enqueue(9)
print(my_queue)

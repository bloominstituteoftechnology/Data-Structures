
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?c
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            removed_val = self.storage.remove_from_head()
            # self.storage.remove_from_head()
            self.size -= 1
            return removed_val
        elif self.size == 0:
            return None

    def len(self):
        return self.storage.length


my_queue = Queue()
print(my_queue)
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(6)
my_queue.enqueue(9)
print(my_queue)

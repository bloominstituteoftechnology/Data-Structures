

from doubly_linked_list import DoublyLinkedList
import sys
# sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        result = self.storage.add_to_tail(value)
        self.size = self.storage.length
        return result

    def dequeue(self):
        if self.size > 0:
            result = self.storage.remove_from_head()
            self.size = self.storage.length
            return result
        else:
            return None

    def len(self):
        return self.storage.length


# q = Queue()
# print(q.len(), 0)
# q.enqueue(2)
# print(q.len(), 1)
# q.enqueue(4)
# print(q.len(), 2)
# q.enqueue(6)
# q.enqueue(8)
# q.enqueue(10)
# q.enqueue(12)
# q.enqueue(14)
# q.enqueue(16)
# q.enqueue(18)
# print(q.len(), 9)

# print(q.dequeue(), 2)
# print(q.len(), 8)
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.len(), 0)

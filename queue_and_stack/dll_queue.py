from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = len(self.storage)

    def dequeue(self):
        val = self.storage.remove_from_tail()
        self.size = len(self.storage)
        return val

    def len(self):
        return self.size

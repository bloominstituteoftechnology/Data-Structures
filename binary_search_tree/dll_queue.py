from doubly_linked_list import DoublyLinkedList as link


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = link()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        value = self.storage.remove_from_tail()
        self.size -= 1
        return value

    def len(self):
        return self.size




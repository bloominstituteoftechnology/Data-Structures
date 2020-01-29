from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        # cuz data is in order and we don't need to access the middle
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        return True

    def dequeue(self):
        if self.len() > 0:
            return self.storage.remove_from_tail()
        return None

    def len(self):
        return len(self.storage)

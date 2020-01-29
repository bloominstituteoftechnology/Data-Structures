from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # cuz data is in order and we don't need to access the middle
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        return True

    def pop(self):
        if self.len() > 0:
            return self.storage.remove_from_head()
        return None

    def len(self):
        return len(self.storage)

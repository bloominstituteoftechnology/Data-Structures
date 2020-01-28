from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.list = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.list.add_to_head(value)

    def pop(self):
        if self.size < 1:
            return
        self.size -= 1
        return self.list.remove_from_head()

    def len(self):
        return self.size

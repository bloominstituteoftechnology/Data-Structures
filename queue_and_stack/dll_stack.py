from doubly_linked_list import DoublyLinkedList as link

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = link()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.storage.remove_from_tail()


    def len(self):
        return self.size

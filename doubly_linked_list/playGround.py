-----
    import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()


    def push(self, value):
        newNode = Node(value,None, None)
        if not self.storage.head and not self.storage.tail:
            self.storage.head = self.storage.tail = newNode
        else:
            self.storage.add_to_tail(value)
        
        self.size = self.storage.length

    def pop(self):
        if not self.storage.tail:
            return False

        self.storage.remove_from_tail()
        return self.storage.tail.value

    def len(self):
        return self.size

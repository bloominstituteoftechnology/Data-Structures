import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#LIFO
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        self.storage.remove_from_head()
        self.size -= 1

    def len(self):
        return self.size

stack = Stack()
stack.push(34)
stack.push(45)
stack.push(14)
stack.pop()
print(f'length: {stack.len()}')

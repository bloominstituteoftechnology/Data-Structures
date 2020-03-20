from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode
# import sys
# sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        # self.size += 1

    def pop(self):
        return self.storage.remove_from_head()
        # if self.size > 0:
        #     removed_val = self.storage.remove_from_head()
        #     self.size -= 1
        #     return removed_val

    def len(self):
        return self.storage.length

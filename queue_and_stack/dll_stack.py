import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.height += 1
        if self.top:
            self.top.insert_after(value)
            self.top = self.top.next
        else:
            self.top = ListNode(value)
    def pop(self):
        if self.height:
            value = self.top.value
            head = self.top
            self.top = self.top.prev
            head.delete()
            self.height -= 1
            return value
        else:
            return None

    def len(self):
        return self.height

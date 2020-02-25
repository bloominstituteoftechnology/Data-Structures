# how do you find and return the middle node of a singly linked list in one pass?

# you do not have access to the length of the list, if the list is even, return first of two middle nodes
# you may not store in another data structure, including another linked list
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode


class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        newhead = ListNode(value):
        if not self.head:
            self.head = newhead
            self.tail = newhead
        else:
            new.next = self.head
            self.head = newhead
        self.length += 1

    def remove_from_head(self):
        if not self.head:
            return
        val = self.head.value
        if self.head is self.tail:
            self.head, self.tail = None, None
            self.length = 0
            return val
        self.head = self.head.next
        self.length -= 1
        return val

    def add_to_tail(self, value):
        new = ListNode(value)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length += 1 

    def remove_from_tail(self):
        if not self.tail:
            return
        val = self.tail.value
        if self.tail is self.head:
            self.tail, self.head = None, None
            self.length = 0
            return val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.length -= 1
        return val

class getMiddle:
    def __init__(self):
        self.thru = Sin
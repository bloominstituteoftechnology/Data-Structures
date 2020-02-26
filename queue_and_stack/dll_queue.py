import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def dequeue(self):
        if self.length > 0:
            value = self.head.value
            head = self.head
            self.head = self.head.next
            head.delete()
            self.length -= 1
            return value
        else:
            return None

    def len(self):
        return self.length

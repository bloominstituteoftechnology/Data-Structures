import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        node = ListNode(value)
        if self.storage.head is not None:
            next_node = self.storage.head.next
            self.storage.head.next = node
            node.prev = self.storage.head
            node.next = next_node
            next_node.prev = node
        else:
            self.storage.head = node

    def dequeue(self):
        pass

    def len(self):
        pass

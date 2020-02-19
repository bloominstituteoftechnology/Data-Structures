import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode


class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        return self.storage.add_to_tail(ListNode(value))

    def dequeue(self):
        return self.storage.remove_from_head()
        
    def len(self):
        return self.storage.length

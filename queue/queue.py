import sys
sys.path.append('../linked_list')
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.storage.head is None:
            return None
        else:
            old_head = self.storage.head.value
            self.storage.remove_head()
            return old_head

    def len(self):
        head = self.storage.head
        if head is None:
            return 0
        elif head.get_next() is None:
            return 1
        else:
            count = 1
            while head.get_next() is not None:
                count += 1
                head = head.get_next()
            return count


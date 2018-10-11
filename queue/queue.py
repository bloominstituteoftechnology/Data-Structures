import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        LinkedList.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        elif self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None


    def len(self):
        # since we have a size var we increment/decrement when adding/removing have the length
        return self.size

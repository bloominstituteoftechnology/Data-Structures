from singly_linked_list import LinkedList
import sys
sys.path.append('../singly_linked_list/')


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        value == self.storage.add_to_head(value)
        self.size += 1
        return value

    def pop(self):
        if self.size == 0:
            return None
        value = self.storage.remove_head()
        self.size -= 1
        return value

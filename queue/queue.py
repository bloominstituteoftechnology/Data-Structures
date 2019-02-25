import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

from doubly_linked_list.doubly_linked_list import ListNode  # nopep8
from doubly_linked_list.doubly_linked_list import DoublyLinkedList  # nopep8


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        try:
            return self.storage.pop(0)
        except IndexError:
            pass

    def len(self):
        return len(self.storage)

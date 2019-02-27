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

from doubly_linked_list.doubly_linked_list import DoublyLinkedList  # nopep8


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        item = self.storage.remove_from_head()
        if item:
            self.size -= 1
            return item
        else:
            return None

    def len(self):
        return self.size

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


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.entries = 0
        self.entries = {}
        self.queue = DoublyLinkedList()

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key):
        try:
            node = self.entries[key]
            self.queue.move_to_front(node)
            return node.value
        except KeyError:
            return None

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """

    def set(self, key, value):
        if self.entries == self.limit:
            lru_val = self.queue.remove_from_tail()
            self.entries.pop(lru_val)

        node = self.queue.add_to_head(value)
        self.entries[key] = node

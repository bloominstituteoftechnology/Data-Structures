from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
      self.limit = limit
      self.length = 0
      self.max_number = 0
      self.storage = {}
      self.cache = DoublyLinkedList(None)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
      if key not in self.storage.keys():
        return None
      # Store the value, delete the key from the cache and then readd it as the newest(first) value 
      value = self.storage[key].value
      del self.storage[key]
      self.storage[key] = value

      # Move the item to the end of the DLL
      self.cache.move_to_end(self.storage[key])
      return f"{self.storage[key]}, {self.storage[key].value}"
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
      if self.length == self.limit:
        del self.storage.keys()[0]
        self.cache.remove_from_head()
      # Will make a new key if it doesn't exist, and replace the value if the key does exist
      self.storage[key] = value
      self.cache.add_to_head((key, value))
      self.length += 1

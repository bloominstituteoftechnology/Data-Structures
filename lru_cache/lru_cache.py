import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.cache = {}
        self.limit = limit
        self.priority = DoublyLinkedList()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            self.priority.move_to_front(self.cache[key]["priority"])
            return self.cache[key]["value"]
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
        if key in self.cache or len(self.cache) < self.limit:
            if key in self.cache:
                self.priority.move_to_front(self.cache[key]["priority"])
            else:
                self.priority.add_to_head(key)
            self.cache[key] = {
                "value": value,
                "priority": self.priority.head   
            }
        else:
            last = self.priority.remove_from_tail()
            del self.cache[last]
            self.cache[key] = {
                "value": value,
                "priority": self.priority.head
            }
            self.priority.add_to_head(key)


lru = LRUCache(3)
lru.set("a",1)
lru.set("b", 2)
lru.set("c", 3)
lru.set("d", 4)
lru.set("c", 5)

print(lru.cache)
lru.get("b")
print(lru.priority)
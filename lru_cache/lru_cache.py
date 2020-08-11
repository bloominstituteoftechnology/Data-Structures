import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes (limit) it
    can hold, the current number of nodes it is holding (nodes), a doubly-
    linked list that holds the key-value entries in the correct
    order (dll), as well as a storage dict that provides fast access
    to every node stored in the cache (cache).
    """
    def __init__(self, limit=10):
        self.nodes = 0  # number of nodes
        self.cache = {}  # fast access to nodes
        self.dll = DoublyLinkedList()
        self.limit = limit  # node limit
        pass

    """
    Retrieves the value associated with the given key. 
    
    Also needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        print('lru_cache.get')
        if key in self.cache:
            node = self.cache[key]
            value = node.value[1]
            # move node to head (front of list)
            self.dll.move_to_front(node)
            return value
        else:
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
        print('lru_cache.set')
        # checks if the node exists in the cache
        # node DOES exist in cache
        if key in self.cache:
            node = self.cache[key]
            # move node to head (front of list)
            self.dll.move_to_front(node)
            node.value = (key, value)
        # node does NOT exist in cache
        else:
            # check if node count is at the limit
            if self.nodes == self.limit:
                del self.cache[self.dll.tail.value[0]]
                self.dll.remove_from_tail()
                self.nodes -= 1

            self.dll.add_to_head((key, value))
            self.cache[key] = self.dll.head
            self.nodes += 1
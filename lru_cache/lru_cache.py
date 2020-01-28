import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the
    max number of nodes it can hold, == limit
    the current number of nodes it is holding, == current_node_count
    a doubly-linked list that holds the key-value entries in the correct
    order,
    as well as a storage dict that provides fast access to every node stored in the cache. == storage_dict
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current_node_count = 0
        self.storage = DoublyLinkedList()
        # should this = something else
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        for i in self.storage:
            s

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
        pass

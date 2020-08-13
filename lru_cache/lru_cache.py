# python3 lru_cache/test_lru_cache.py -v

from doubly_linked_list.doubly_linked_list import ListNode, DoublyLinkedList

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
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if self.size == 0:
            return
        else:
            if key in self.storage.keys():
                self.order.move_to_front(ListNode(key))
                return self.storage[key]
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
        if self.size == self.limit:
            if key in self.storage.keys():
                self.storage[key] = value
                self.order.move_to_front(ListNode(key))
            else:
                self.order.remove_from_tail()
                self.storage.pop(self.order.remove_from_tail().value)
                self.order.add_to_head(ListNode(key))
                self.storage[key] = value
        else:
            if key in self.storage.keys():
                self.storage[key] = value
                self.order.move_to_front(ListNode(key))
            else:
                self.size += 1
                self.order.add_to_head(ListNode(key))
                self.storage[key] = value

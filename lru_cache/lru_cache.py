from doubly_linked_list import DoublyLinkedList, ListNode

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
        self.hash = {}
        self.storage = DoublyLinkedList()
        self.size = 0
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.hash:
            self.storage.move_to_front(self.hash[key])
            return self.storage.head.value
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
        
        if key in self.hash:
            self.storage.move_to_front(self.hash[key])
            self.get(key)
        if self.size < self.limit:
            self.storage.add_to_head(ListNode(value))
            self.size += 1
            self.hash[key] = ListNode(value)
        if self.size >= self.limit:
            temp = {key:val for key, val in self.hash.items() if val.value != self.storage.tail.value.value}
            self.hash = temp
            del temp
            self.storage.remove_from_tail()
            self.storage.add_to_head(ListNode(value))
            self.hash[key] = ListNode(value)

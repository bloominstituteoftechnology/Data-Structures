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
        self.limit: int = limit
        self.storage = DoublyLinkedList()
        self.lookup = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        node = self.lookup.get(key)

        if node:
            self.storage.move_to_front(node)
            entry: tuple = node.value
            return entry[1]
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

        node = self.lookup.get(key)
        if node: # value stored already
            self.storage.delete(node) # so delete it from storage

        if len(self.storage) == self.limit: # at limit
            oldest_entry: tuple = self.storage.tail.value 
            oldest_key = oldest_entry[0] # grab key from tail
            self.lookup.pop(oldest_key) # remove key from lookup
            self.storage.remove_from_tail # delete tail

        self.storage.add_to_head((key, value)) # store key and value in tuple in storage
        self.lookup[key] = self.storage.head # set key in lookup to find node in constant time
            

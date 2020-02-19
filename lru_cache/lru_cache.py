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
        self.cache = DoublyLinkedList()
        self.limit = limit
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            current = self.cache.head # Set startin point to head

            while current.key is not key: # Iterate until we find the node
                current = current.next
            
            self.cache.move_to_front(current) #set node to front
            return current.value #return the value

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
        if key in self.storage.keys(): # Check if key exists in cache
            self.storage[key] = value
            current = self.cache.head
            while current.key is not key:
                current = current.next
            current.value = value

        elif self.cache.length < self.limit: # Check if cache is full, if not, add to head
            self.cache.add_to_head(key, value)
            self.storage[key] = value
        else: # if cache is full remove last one and add to head
            old_key, old_value = self.cache.remove_from_tail()
            del self.storage[old_key]
            self.cache.add_to_head(key, value)
            self.storage[key] = value
        

import sys
sys.path.append('../doubly_linked_list/')
from doubly_linked_list import DoublyLinkedList

#Behaves like a doubly linked Queue list
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
        self.head = None
        self.tail = None
        self.list = DoublyLinkedList()
        self.storage = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Size condition
        if key not in self.storage.keys() or self.size == 0:
            return
        
        self.list.move_to_front(self.storage[key])

        return self.storage[key].value[1]

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
        if key in self.storage.keys():
            self.storage[key].value[1] = value
            self.list.move_to_front(self.storage[key])
        else:
            if self.size == self.limit:
                #Delete tail node 
                # How do I get rid of the node's key in the storage dict?
                remove_key = self.list.remove_from_tail()[0] #this returns the value that was removed, should I make the stored values be {key:value} instead of value?
                self.storage.pop(remove_key)
                self.size -= 1
            self.list.add_to_head([key,value])
            self.storage[key] = self.list.head     
        self.size += 1
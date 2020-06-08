import sys
sys.path.append('../doubly_linked_list')
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
        self.limit=limit
        self.storage={}
        self.dll=DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key is present in dict move the key val pair to front and 
        # return the val corresponding to key
        #else return None
        if key in self.storage:
            self.dll.move_to_front(self.storage[key])
            return self.dll.head.value['value']
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
        # if key not present in dict create a node and add to front of dll and make the head point to it
        # if key is present in dict move to head and make dll head point to it, overwrite its value to 
        # the vakue set by argument
        #if dll exceeds limit remove tail node and return its value.
        if key not in self.storage:
            self.dll.add_to_head({'key':key,'value':value})
            self.storage[key]=self.dll.head
        else:
            self.dll.move_to_front(self.storage[key])
            self.dll.head.value={'key':key,'value':value}
            self.storage[key]=self.dll.head
        
        if len(self.storage)>self.limit:
            self.storage.pop(self.dll.tail.value['key'])
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
        self.size = 0
        # tail is most recently used, head is least recently used
        self.order = DoublyLinkedList()
        # cache
        self.storage = {}
        # would the below work?
        # self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # tests if the key is defined in the dict() we are using as cache
        if key in self.storage:
            # return the node from the cache, not the linked list
            node = self.storage[key]
            # move the returned node to the end of the list (most recently used)
            # naturally pushes the least recently used to the back
            self.order.move_to_end(node)
            # what is happening here in python? got this code from a student solution
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. 
    
    The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. 
    
    Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if the key is already in the dict, update it and move the node to tail
        if key in self.storage:
            # KEY: (key, value) 
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
        # # else, we care about size
        else:
            if self.size == self.limit: #make room by removing old
                node = self.order.head
                self.storage.pop(node.value[0]) # pop head's key from dict
                self.order.remove_from_head() # no need to adjust size, new is added
            else:
                self.size += 1
            # add the new (key, value) tuple to the list and key, value pair to the dict
            self.order.add_to_tail((key, value))
            #get my node object
            node = self.order.tail
            #put node object in dictionary
            self.storage[key] = node

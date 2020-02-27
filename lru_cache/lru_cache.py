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
        self.storage = dict()
        self.order = DoublyLinkedList()



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            #this is setting the node to the key in self.storage
            node = self.storage[key]
            #this is moving the node to the end of the cache
            self.order.move_to_end(node)
            #then returns the value of such key if it exists
            return node.value[1]
            # else it returns nothing...
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
        # Create a node if key not found
        # Move node to front if key found 
        # If full remove last node from linked list AND dictionary 
        if key in self.storage: 
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return 
        
        #this checks to see if the cache is full
        if self.size == self.limit: 
            #this will remove the oldest entry from the dictionary 
            del self.storage[self.order.head.value[0]]
            #does the same but for the linked list
            self.order.remove_from_head()
            self.size -= 1

        #this adds the key and value pair to the linked list
        self.order.add_to_tail((key, value))
        #Adds the key and value pair to the dictionary 
        self.storage[key] = self.order.tail
        #increments the size by 1
        self.size += 1
       



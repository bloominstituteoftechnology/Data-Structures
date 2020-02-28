import sys
sys.path.append('../doubly_linked_list') 
from doubly_linked_list import DoublyLinkedList


#can be used for frequently visited sites
#Browser cache so it remembers and moves quicker 
#store it in cache instead
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10): #initalize yo self bruh
        self.limit = limit 
        self.size = 0 #dont have anything yet so start at 0 
        self.storage = {} #dict
        self.order = DoublyLinkedList()  #spec says need storage and dll

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    #if you look at tests, you need both set and get
    def get(self, key):
        
        if key in self.storage:
            print(key)
            node = self.storage[key]
            print(node)
        
            if node is not None:
                self.order.move_to_end(node)
                return node.value[1]
            
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
       #check and see if key is in dict
        if key in self.storage:
              #if it is 
            node = self.storage[key] #grab the whole node 
                #overwrite the value 
            node.value = (key, value)
                #move it to the end
            self.order.move_to_end(node)
            #nothing else so exit
            return 
        
            #check and see if cache is full 
        if self.size == self.limit:
              #remove oldest entry from dict and LL
              del self.storage[self.order.head.value[0]]
              self.order.remove_from_head()
              #reduce the size
              self.size = -1
              

            #add to ll(key, value)
        self.order.add_to_tail((key, value))
            #add key and val to dict
        self.storage[key] = self.order.tail
            #increment size
        self.size += 1

          
        

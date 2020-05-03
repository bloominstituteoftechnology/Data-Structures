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
        self.storage = {}
        self.limit = limit
        self.ordering = DoublyLinkedList()
        self.size = 0


        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        
        if key in self.storage:
                node = self.storage[key]
                self.ordering.move_to_end(node)
                return node.value[1]
        else:
                # print("None 34")
                return None
       
           

    # """
    # Adds the given key-value pair to the cache. The newly-
    # added pair should be considered the most-recently used
    # entry in the cache. If the cache is already at max capacity
    # before this entry is added, then the oldest entry in the
    # cache needs to be removed to make room. Additionally, in the
    # case that the key already exists in the cache, we simply
    # want to overwrite the old value associated with the key with
    # the newly-specified value.
    # """

    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.ordering.move_to_end(node)
            return
        if self.size == self.limit:
            oldest_key = self.ordering.head.value[0]
            del self.storage[oldest_key]
            self.ordering.remove_from_head()
            self.size -=1
        self.ordering.add_to_tail((key, value))
        self.storage[key] = self.ordering.tail
        self.size += 1
        
    # def set(self, key, value):
    #     # print(self.index, "self.index", )
    #     if self.index == 0:
    #         self.key = key
    #         return self.storage.add_to_head(value)
    #     elif self.index < self.limit:
    #         self.key = key
    #         return self.storage.add_to_tail(value)
    #     self.index += 1
        
        
        
# new_que = LRUCache(3)

# new_que.set('one', '1')
# new_que.set('two', '2')


# new_que.get('one')

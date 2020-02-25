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
        self.storage = DoublyLinkedList()
        self.hash_table = {}
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if structure has value corresponding to key, return value
        if key in self.hash_table:
            value = self.storage.head  # Starting Point

            while value.key is not key:  # 'Loop' to find the correct match
                value = value.next  # Call next while loops continues until case is matched

            self.storage.move_to_front(value)  # Move node to the front
            return value.value
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
        # overwrite existing key value pair
        if key in self.hash_table:
            # update the value in the hash table
            self.hash_table[key] = value
            # look at the items in the DLL
            dll_node = self.storage.head
            # we have to find the node that has that same key in order to update it
            while dll_node.key is not key:
                # keep going
                dll_node = dll_node.next
            # update that node's value
            dll_node.value = value

        # check length of cash vs limit
        elif self.storage.length < self.limit:
        # add to the head
            self.storage.add_to_head(key, value)
            self.hash_table[key] = value
        
        else:
            key_to_remove, v = self.storage.remove_from_tail()
            del self.hash_table[key_to_remove]
            self.storage.add_to_head(key, value)
            self.hash_table[key] = value


        


# cache entries stored in DLL
# hash table that points to value
# head of DLL is most recently used
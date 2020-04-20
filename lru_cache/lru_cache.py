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
        self.storage = DoublyLinkedList()
        self.lookup = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if self.lookup.get(key):
            # Move the key-value pair to the DLL tail.
            # 1. Take the node out of its prev place in DLL
            self.lookup[key].delete()
            # 2. Add it to DLL as new tail
            self.storage.add_to_tail(self.lookup[key].value, key)
            # Return the value associated with that key.
            return self.lookup.get(key).value
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
        # if not self.lookup[key]:
        if not self.lookup.get(key):
            # In this case, not already in cache

            if self.size == self.limit:
                # In this case, the cache is at max capacity, so oldest value has to be evicted.
                # Remove it from DLL storage
                self.storage.head = self.storage.head.next
                oldest = self.storage.remove_from_head()
                # Remove it from dict
                self.lookup.pop(oldest[0])

            # Creates a new node and inserts it as new DLL tail
            self.storage.add_to_tail(value, key)
            # Add it to the dict
            self.lookup[key] = self.storage.tail
            # Increment the LRU cache size
            self.size += 1

        else:
            # Update LRU cache with new value
            self.lookup[key].value = value
            # Move it to the tail
            # 1. Take the node out of its prev place in DLL
            self.lookup[key].delete()
            # 2. Add it to DLL as new tail
            self.storage.add_to_tail(value, key)


my_cache = LRUCache(3)
my_cache.set('item1', 'a')
print(my_cache.get('item1'))
print(my_cache.lookup['item1'].value)
print(my_cache.limit)
print(my_cache.size)

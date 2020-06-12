import collections

class LRUCache:                                                            #<<<
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self._limit = limit
        self._size = 0
        self._cache = collections.OrderedDict()

    @property
    def limit(self):
        return self._limit
    @property
    def size(self):
        return self._size
    @property
    def storage(self):
        return self._storage

    @limit.setter
    def limit(self, x):
        self._limit = x
    @size.setter
    def size(self, x):
        self._size = x
    @storage.setter
    def storage(self, x):
        self._storage = x

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        try:
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
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
        try:
            self._cache.pop(key)
        except KeyError:
            if len(self._cache) >= self._limit:
                self._cache.popitem(last=False)
        self._cache[key] = value


if __name__ == "__main__": #>>> <PASS>
    pass
import sys
sys.path.append('../queue')
from queueue import Queue


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        # key: item's key, value: node in Linked list
        self.cache = {}
        self.queue = Queue()
        # nodes in the queue
        # value: item's value

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the top of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache. 
    """
    # doesn't delete the key
    def get(self, key):
        node = self.cache.get(key, None)
        if node:
            self.queue.make_low_priority(node)
            return node.value
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
        old_value = self.cache.get(key, None)
        if old_value:
            node = self.cache[key]
            node.value = value
            self.cache[key] = self.queue.make_low_priority(node)
        else:
            if len(self.cache) == self.limit:
                oldest_key, _ = self.queue.dequeue()
                self.cache.pop(oldest_key, None)
            node = self.queue.enqueue(value, key)
            self.cache[key] = node

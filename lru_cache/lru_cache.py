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
        self.max = limit
        self.cur = 0
        # if cur == max, adding should remove LRU
        self.storage = DoublyLinkedList()
        # self.storage.head
        # self.storage.tail
        # self.storage.length
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            node = self.cache[key]
            self.storage.move_to_front(node)
            return node.value[1]

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
        # add key/value pair to the cache
        if key in self.cache:
            self.cache[key].value[1] = value
        else:
            self.storage.add_to_head([key, value])
            self.cache[key] = self.storage.head

            self.cur += 1

            if self.cur > self.max:
                value = self.storage.remove_from_tail()
                key = value[0]
                del self.cache[key]

                self.cur -= 1

        # add to head of self.storage
        # i need to remove from dll's tail
        #   i need to remove the tail's node from the cache

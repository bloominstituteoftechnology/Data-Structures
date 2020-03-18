import sys
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
        self.length = 0
        self.ddl = DoublyLinkedList()
        self.map = {}

    def __str__(self):
        if self.length:
            return 'empty'
        print(self.ddl)
        output = ''
        for key in self.map:
            output += f'( {key}:{self.map[key]} )'
        return output
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # update items if used
        # find the key in order structure, and move to front of
        if key in self.map:  # node.value = (apple, 'is a fruit')
            node = self.map[key]
            self.ddl.move_to_front(node)
            return node.value[1]
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
        # remove items that arn'et used
        # key is not in strogage, and limit has not been hit yet
        # add the key to the front of the order structures

        if key in self.map: # item1
            node = self.map[key]
            node.value = (key, value)
            self.ddl.move_to_front(node)
            return
        if self.length == self.limit:
            del self.map[self.ddl.tail.value[0]]
            self.ddl.remove_from_tail()
            self.length -=1

        self.ddl.add_to_head((key, value))
        self.map[key] = self.ddl.head
        self.length += 1

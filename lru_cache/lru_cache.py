import sys
sys.path.append('../doubly_linked_list')
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
        self.list = DoublyLinkedList()
        self.storage = {}
        self.length = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):                         # passing in the key
    # if in storage
        if key in self.storage:                         # if it is in the storage, we move forward
            node = self.storage[key]                    # set the node to the self.storage[key], listnode object
            self.list.move_to_end(self.storage[key])    # move to the end using the DoublyLinkedList
            return node.value[1]                        # return the value of the node object
        else:
            return None
# can create any kind of node that we want, we can give it any name that we want
# list node was created specifically to be used in DoublyLinkedList
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
        if key in self.storage:                   # if key in storage
            node = self.storage[key]              # set the node at the key
            node.value = (key, value)             # the value of the node is equal to key and the value tuple
            self.list.move_to_end(node)           # we move it to the end of the list bc it's most recently used
            return

        if self.length == self.limit:                   # however, if the list is full
            del self.storage[self.list.head.value[0]]   # we delete the head because that is the least used item
            self.list.remove_from_head()                # we perform the remove from head function
            self.length -= 1

        self.list.add_to_tail((key, value))             # this the main funciton of adding the value to tail
        self.storage[key] = self.list.tail              # store the key from tail since we already added it
        self.length += 1                                # increase the length by 1

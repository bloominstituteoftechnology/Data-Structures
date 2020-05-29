import sys

sys.path.append("../doubly_linked_list")

from doubly_linked_list import DoublyLinkedList, ListNode
from collections import OrderedDict


class LRUCache(OrderedDict):

    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, maxsize=128, /, *args, **kwds):
        super().__init__(*args, **kwds)
        self.maxsize = maxsize
        self.dllist = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        try:
            value = super().__getitem__(key)
            self.move_to_end(key)
            existing_node = self.dllist.get_node(value)
            self.dllist.move_to_front(existing_node)
            # return value
            return self.dllist.head.value
        except:
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
        if key in self:
            existing_node = self.dllist.get_node(self[key])
            self.move_to_end(key)
            # self.dllist.delete(existing_node)
            # self.dllist.add_to_head(value)
            self.dllist.move_to_front(existing_node)

        super().__setitem__(key, value)
        self.dllist.add_to_head(value)

        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
            self.dllist.remove_from_tail()


# class LRUCache(OrderedDict):

#     def __init__(self, maxsize=128, /, *args, **kwds):
#         self.maxsize = maxsize
#         super().__init__(*args, **kwds)

#     def get(self, key):
#         try:
#             value = super().__getitem__(key)
#             self.move_to_end(key)
#             return value
#         except:
#             return None

#     def set(self, key, value):
#         if key in self:
#             self.move_to_end(key)
#         super().__setitem__(key, value)
#         if len(self) > self.maxsize:
#             oldest = next(iter(self))
#             del self[oldest]

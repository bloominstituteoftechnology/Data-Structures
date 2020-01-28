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
        self.list = DoublyLinkedList()
        self.limit = limit
        self.length = 0
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if the key is not in the cache
        if key not in self.storage_dict:
            # return none
            return None
        # if the key is in the cache
        else:
            # retrive the node, get the value
            existing_node = self.storage_dict[key]
            kv_pair = existing_node.value
            # move to front of list
            self.list.move_to_front(existing_node)
            # return value
            return kv_pair[1]

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
        # if the key is already in the cache
        if key in self.storage_dict:
            # TODO: update value in link list
            existing_node = self.storage_dict[key]
            existing_node.value = (key, value)
            # TODO: move to the front of the list
            self.list.move_to_front(existing_node)
            print('storage dict edit entry', self.storage_dict)
        # if the key is not already in the cache
        else:
            # make a tuple with the key value pair
            kv_tuple = (key, value)
            # insert it into the list
            new_node = self.list.add_to_head(kv_tuple)
            # save a reference in the dictionary
            # self.storage_dict.update({key, new_node})
            self.storage_dict[key] = new_node
            self.length += 1
            print('storage dict new entry', self.storage_dict)
        # while the length of the cache is past the limit
        while self.length > self.limit:
            # remove the stuff at the end
            deleted_kv = self.list.remove_from_tail()
            # remove entries from dict
            del self.storage_dict[deleted_kv[0]]
            self.length -= 1
            print('storage dict after delete', self.storage_dict)

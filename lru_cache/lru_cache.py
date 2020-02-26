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
        self.cache = DoublyLinkedList()
        self.limit = limit
        # storing our key + value in {}
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            # setting the head node to current value
            current_value = self.cache.head
            # looks for if the current_value.key matches the value of key, if it does not match then it traverses until the current_value.key matches the key
            while current_value.key is not key:
                current_value = current_value.next
            # taking current_value and setting it to the front aka the head node
            self.cache.move_to_front(current_value)
            return current_value.value
        # if key is not in storage, return None
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
        # if the key is in our storage, we're assigning it to value
        # setting current_value to the head node
        if key in self.storage.keys():
            self.storage[key] = value
            current_value = self.cache.head
            # checking to see if the value of the key matches the keys value, if it does not match then it'll traverse through until the value matches
            while current_value.key is not key:
                current_value = current_value.next
            # setting the value of the list node to the passed in value
            current_value.value = value
            self.cache.move_to_front(current_value)
            self.storage[key] = self.cache.head
        # checking to see if our cache is less than the limit, adding that value to the head and storing the key to value
        elif self.cache.length < self.limit:
            self.cache.add_to_head(key, value)
            self.storage[key] = self.cache.head
        # if our cache.length > the limit, we are removing it the value at the tail and deleting it
        # then taking our node we're trying to insert and adding that to the head and storing the key index value to our previous value
        else:
            # this is deleting it from the linked list
            previous_value, previous_key  = self.cache.remove_from_tail()
            # deleting variable from the cache
            del self.storage[previous_key]
            self.cache.add_to_head(key, value)
            self.storage[key] = self.cache.head




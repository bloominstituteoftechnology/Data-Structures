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
        self.held = 0
        self.linked_list = DoublyLinkedList()
        self.hash = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        pass

    # use hash to return quickly

    # rotate through linked list find key value pair
    # save it in temp
    # delete from list
    # move temp to head
    # should always be enough room

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
        # check to see if item exists in the list:

        # access dict with key return false if it doesn't
        # if it exists update the dict value
        # go through linked list and update value in linked_list

        # if it doesn't exist:

        # if limit is full:

        # delete capture the tail
        # delete that tail
        # delete that value from hash

        # full or not full add it to linked list
        # add it to the head of the list
        # add it to the head of the linked list and
        # ad it to the hash as a key value pair

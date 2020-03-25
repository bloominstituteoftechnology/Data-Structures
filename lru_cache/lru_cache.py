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
        self.storage = DoublyLinkedList()
        self.limit = limit  # max number of nodes
        self.cache = {}

        # Tail - Head
        # [4,2,3,1]
        # [ {"item1": "a"}, {"item2": "b"}, {"item3": "c"} ]
        # most recently used - least recently used
        # FIFO - Queue

    """
	Retrieves the value associated with the given key. Also
	needs to move the key-value pair to the end of the order
	such that the pair is considered most-recently used.
	Returns the value associated with the key or None if the
	key-value pair doesn't exist in the cache.
	"""

    def get(self, key):
        # Retrieves the value associated with the given key

        # Also needs to move the key-value pair to the end of the order such that the pair is considered most-recently used.
        # Returns the value associated with the key or None if the key-value pair doesn't exist in the cache.
        if key in self.cache:
            node = self.cache[key]
            self.storage.move_to_front(node)
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
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            return self.storage.move_to_front(node)

        if len(self.storage) == self.limit:
            del self.cache[self.storage.tail.value[0]]
            self.storage.remove_from_tail()

        self.storage.add_to_head((key, value))
        self.cache[key] = self.storage.head

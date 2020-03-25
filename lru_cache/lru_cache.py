from doubly_linked_list import DoublyLinkedList, ListNode

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
        self.limit = limit
        self.nodes = 0
        # dictionary serves as hash map
        self.dict = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.storage.delete(node)
            self.storage.add_to_head(node)
            return node.value[key]
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
        if key in self.dict:
            node = self.dict[key]
            node.value[key] = value
        else:
            new_node = ListNode({key: value})
            if self.nodes == self.limit:
                tail_key = [i for i in self.storage.head.value.value][0]
                # print('the tail key is ', tail_key)
                self.storage.remove_from_head()
                del self.dict[tail_key]
            self.storage.add_to_head(new_node)
            self.dict[key] = new_node
        self.nodes += 1

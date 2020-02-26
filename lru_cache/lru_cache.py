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
        self.current_no_of_nodes = 0
        self.cache = {}
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            node = self.storage.head
            while node:
                eachKey = list(node.value.keys())[0]
                if eachKey == key:
                    self.storage.move_to_end(node)
                    break
            return value


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
            node = self.storage.head
            while node:
                # eack key from the LRU cache DLL
                eachKey = (node.value.keys())[0]
                if eachKey == key:
                    # Update to LRU cache
                    node.value[key] = value
                    # Add to memoization cache
                    self.cache[key] = value
                    break
                node = node.next

        # remove from head to make room
        if self.current_no_of_nodes == self.limit:
            self.storage.remove_from_head()
        # add to LRU 
        self.storage.add_to_tail({ key: value })
        # add to memoization cache
        self.cache[key] = value
        self.current_no_of_nodes += 1

    def __str__(self):
        return f'storage: {self.storage.head.value} cache: {self.cache}'

        

# cache = LRUCache(3)
# cache.set('item1', 'a')
# cache.set('item1', 'b')
# cache.set('item3', 'c')
# print(cache.__str__())



        # self.storage.add_to_tail({key: value})

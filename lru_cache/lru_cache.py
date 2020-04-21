from doubly_linked_list import DoublyLinkedList

class LRUCache(DoublyLinkedList):
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.size = 0
        self.keys = {}
        self.storage = DoublyLinkedList()
        self.limit = limit


    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        # return None if list hasn't been built
        if self.size==0:
            return None
        # if key not found return None
        if key not in self.keys:
            return None

        self.storage.add_to_tail(key)

        value = self.keys[key]
        return value




    def set(self, key, value):
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

        if self.size < self.limit:
            if self.storage.head == None:
                #add key to list head
                self.storage.add_to_head(key)
                #add key in key list
                self.keys[key] = value
                self.size += 1
            else:
                self.storage.add_to_tail(key)
                self.keys[key] = value
                self.size += 1

        elif self.size >= self.limit:
            ktd = self.storage.remove_from_head()
            self.keys.pop(ktd, None)
            self.storage.add_to_tail(key)
            self.keys[key] = value

        else:
            print('how did I get here?')
test = LRUCache(2)
print(test.storage.head)
print(test.size)
print(test.keys)
print('test limit:', test.limit)
test.set('blah', 7)
print(test.keys)
print(test.size)
test.set('bleh', 8)
print(test.keys)
print(test.size)
test.set('bluh', 9)
print(test.keys)
print(test.size)

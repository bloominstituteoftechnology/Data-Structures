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

    # def update(self, key, new = False):
    #     """
    #     places keys at the tail in storage, then iterates through and removes
    #     the old value if new is set to False.
    #     """
    #     self.storage.add_to_tail(key)
    #
    #     if new == False:
    #         current = self.storage.head
    #         # val = self.head.value
    #         # Loop  through nodes
    #         done = False
    #         while done != True:
    #             # compare value in node to max found
    #             if current.value == key:
    #                 self.storage.delete(self.storage)
    #                 done = True
    #             if current.next == None:
    #                 done = True
    #
    #             current = current.next

        pass


    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        if key in self.keys:
            node = self.keys[key]
            self.storage.move_to_end(node)
        #
        # # if key not found return None
        # if key not in self.keys:
        #     return None
        #
        # # return None if list hasn't been built
        # if self.size==0:
        #     return None
        #
        # self.storage.add_to_tail(key)
        # self.update(key)
        # value = self.keys[key]
            return node.value[1]




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
        if key in self.keys:
            node = self.keys[key]
            node.value = (key, value)
            self.storage.move_to_end(node)
            return
        if self.size == self.limit:
            head = self.storage.head.value[0]
            del self.keys[head]
            self.storage.remove_from_head()
            self.size -=1
        #key is not in cache, and still have room
        self.storage.add_to_tail((key, value))
        self.keys[key] = self.storage.tail
        self.size += 1
        # if self.size < self.limit:
        #     if self.storage.head == None:
        #         #add key to list head
        #         self.storage.add_to_head(key)
        #         #add key in key list
        #         self.keys[key] = value
        #         self.size += 1
        #     else:
        #         self.storage.add_to_tail(key)
        #         if key in self.keys:
        #             self.update(key, True)
        #         else:
        #             self.update(key)
        #         self.keys[key] = value
        #         self.size += 1
        #
        # elif self.size >= self.limit:
        #     ktd = self.storage.remove_from_head()
        #     self.keys.pop(ktd, None)
        #     self.storage.add_to_tail(key)
        #     self.keys[key] = value
        #
        # else:
        #     print('how did I get here?')

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
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.order = DoublyLinkedList()
        # self.limit = limit
        # # self.nodes_in_cache = 0
        # self.cache = DoublyLinkedList()
        # self.storage = {}
        # self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

        # if key in self.storage:
        #     node = self.storage[key]
        #     self.cache.move_to_front(node)
        #     return node.value[1]
        # else:
        #     return None

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
    def set(self, key, value):   # {'item1': node} == node.value == (item1, 1)
        """
        Cases to handle:
        does the key already exist in the cache?
        yes
        no
            are we at a cap or not?
            yes
            no
        """
        if key in self.storage:
            # key here so replace value
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        if self.size == self.limit:
            # option 1, explicit way
            # del self.storage[self.order.head.value[0]]
            # self.order.remove_from_head()

            # # option 2, pythonic way
            del self.storage[self.order.remove_from_head()[0]]
            self.size -= 1


        
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1

        # if key not in self.storage:
        #     # node.key, node.value = key, (key, value)
        #     self.cache.add_to_head((key, value))
        #     self.storage[key] = self.cache.head
        #     self.size += 1
        #     # return

        # if key in self.storage:
        #     node = self.storage[key]
        #     node.value = (key, value)
        #     self.cache.move_to_front(node)
        #     return

        # # if self.cache.length == self.limit:
    
        # self.cache.add_to_head((key, value))
        # self.storage[key] = self.cache.head
        # self.size += 1

        # if self.size == self.limit:
        #     self.cache.remove_from_tail()
        #     self.size -= 1
        #     # return

        # # self.cache.add_to_head((key, value))
        # self.storage[key] = self.cache.head
        
        # if key in self.list:
        #     self.list.move_to_front()

        # else:
        #     if self.list.length == limit:
        #         self.list.remove_from_tail()
        #         self.list.add_to_head()
        #     else:
        #         self.list.add_to_head()

        # if self.cache.length == self.limit:
        #     self.cache.remove_from_tail()
        #     # self.nodes_in_cache -= 1
        #     # node = self.storage[key]
        #     # node.value = (key, value)
        #     # self.cache.add_to_head(node)
        #     return

        # elif key in self.storage:
        #     node = self.storage[key]
        #     # key value pair tuple
        #     # node.value = (key, value)
        #     self.cache.move_to_front(node)
        #     return node
        
        #     # node = self.storage[key]
        #     # node.value = (key, value)
        
        # self.cache.add_to_head((key, value))
        # self.storage[key] = self.cache.head
        # self.nodes_in_cache += 1
        # node = self.storage[key]
        # node.value = (key, value)
        # return node
        
        # return


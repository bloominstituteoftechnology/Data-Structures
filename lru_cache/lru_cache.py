import sys
sys.path.append('../doubly_linked_list')
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
        self.order = DoublyLinkedList()
        self.current_nodes = 0
        self.storage = dict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # print(f'getting key {key}')
        # print('current storage keys:')

        # for index, item in self.storage.items():
        #     print(index, item.value)
        
        if key in self.storage:
            # print('key in storage')
            node = self.storage[key]
            self.order.move_to_front(node)
            # print(f'value to return {node.value[1]}')
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

        # print(f'setting key {key}, value {value}')

        #check for duplicate key-value
        if key in self.storage:
            # print('key in storage')
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return
        
        # if the cache is at the limit delete last element
        if self.current_nodes == self.limit:
            # print(f'deleting {self.order.tail.value}')
            
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.current_nodes -= 1

        #add a node to the cache
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.current_nodes += 1
        


# test = LRUCache(3)

# test.set('item1', 'a')
# test.set('item2', 'b')
# test.set('item3', 'c')

# print(test.get('item1'), 'a')
# test.set('item4', 'd')

# print(test.get('item1'), 'a')

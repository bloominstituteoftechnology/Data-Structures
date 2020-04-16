from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the 1. max number of nodes it
    can hold, 2. the current number of nodes it is holding, 3. a doubly-
    linked list that holds the key-value entries in the correct
    order, 4. as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit  # 1
        # self.size = 0  # 2
        self.order = DoublyLinkedList()  # 3
        self.storage = {}  # 4

    """
    1. Retrieves the value associated with the given key. 2. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    (key, value) tuple
    """

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        else:
            return None
        # if key in self.storage:
        #     item = (key, self.storage[key])
        #     # print(self.dict[key])
        # else:
        #     return None
        #
        # node = self.order.head
        # print("Node!", node)
        #
        # while node.value != item:
        #     print("Compare", node.value, item)
        #     node = node.next
        #     print("new node!", node.value)
        #     if node == None:
        #         return
        # # print(node.value)
        # self.order.move_to_front(node)
        #
        # return self.storage[key]

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
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return

        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head

        if len(self.order) > self.limit:
            node = self.order.remove_from_tail()
            del self.storage[node[0]]

# cache = LRUCache(3)
# cache.set('item1', 'a')
# cache.set('item2', 'b')
# cache.set('item3', 'c')
# print(cache.order.head.value)
# print(cache.order.head.value == ("item3", "c"))
# # assertEqual(self.cache.get('item1'), 'a')
# # cache.set('item4', 'd')
# print("Size", cache.size)
# print("self.storage.length", cache.order.length)
#
# self.assertEqual(self.cache.get('item1'), 'a')
# self.assertEqual(self.cache.get('item3'), 'c')
# self.assertEqual(self.cache.get('item4'), 'd')
# self.assertIsNone(self.cache.get('item2'))
# thing = cache.get("item2")
# print(cache.dict)
# print(thing)

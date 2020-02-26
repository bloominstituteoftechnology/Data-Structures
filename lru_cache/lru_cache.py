from doubly_linked_list import ListNode, DoublyLinkedList

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
        self.length = 0
        self.directory = {}
        self.order = DoublyLinkedList()
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




        # 
        #
        #
        # if key not in self.directory:
        #     return None
        # else:
        #     value = self.directory[key]
        #     pointer = self.mru
        #     while pointer.value != value:
        #         pointer = pointer.prev
        #     self.set(pointer.key, pointer.value, False)
        #     pointer.delete()
        #     return value

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
            self.order.move_to_end(node)
            return

        if self.size == self.limit:
            del self.storage(self.order.head.value[0])
            self.order.remove_from_head()
            self.size -= 1
        self.order.add_to_tail(key, value))
        self.storage[key] = self.order.tail
        self.size += 1


        # if not self.mru and not self.lru:
        #     self.mru = self.lru = ListNode(value=value, key=key)
        # else:
        #     if key in self.directory and trueset == True:
        #         pointer = self.mru
        #         while pointer.value != self.directory[key]:
        #             pointer = pointer.prev
        #         if self.mru == pointer:
        #             self.mru = self.mru.prev
        #         if self.lru == pointer:
        #             self.lru = self.lru.next
        #         pointer.delete()
        #     self.mru.insert_after(value, key)
        #     self.mru = self.mru.next
        #     if self.mru == self.lru:
        #         self.lru = self.mru.prev
        # self.directory[key] = value
        # if trueset:
        #     self.length += 1
        #     if self.length > self.limit:
        #         del self.directory[self.lru.key]
        #         new_first = self.lru.next
        #         self.lru.delete()
        #         self.lru = new_first
        #         self.length -= 1

cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.set('item2', 'z')

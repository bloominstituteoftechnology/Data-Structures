
from doubly_linked_list import ListNode
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
        #node limit to limit ^
        self.limit = limit
        self.size = 0
        self.dictionary = dict()
        self.linkedList = DoublyLinkedList()



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):

        """
        Retreives a value from the cache (will always be positive) at
        the key if the key exists in the cache, otherwise returns -1.
                """
        if key in self.dictionary:
            node = self.dictionary[key]
            self.linkedList.move_to_end(node)
            return node.value[1] #<<< tupples 
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
        """
        Inserts the value at the key or creates a new key:value entry
        if key is not present. When the cache reaches its capacity, it
        invalidates the least recently used item before inserting a new item.
        """
        #if key already exists
        if key in self.dictionary:
            # override the val
            
            node = self.dictionary[key]
            # and where its stored
            node.value = (key, value)
            # then move the node to the tail
            self.linkedList.move_to_end(node)
            #finally done
            return
        # if it reaches the limit then override the first item
        if self.size == self.limit:
            # delete the old one
            del self.dictionary[self.linkedList.head.value[0]] #<<<[0] tupple
            self.linkedList.remove_from_head()
            self.size -= 1
        # and add new item to tail
        self.linkedList.add_to_tail((key, value))
        self.dictionary[key] = self.linkedList.tail
        self.size += 1
            
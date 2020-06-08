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
        self.limit = limit
        self.dll = DoublyLinkedList(None)
        # self.size = self.dll.length
        self.dic = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dic.keys():
            value = self.dic[key]
            checkingnode = self.dll.head
            while checkingnode is not None:
                if checkingnode.key == key:
                    self.dll.move_to_front(checkingnode)
                        
                checkingnode = checkingnode.next

            self.dll.set_tail()
            return value

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
        if key in self.dic.keys():
            
            self.dic.update({key:value})

            checkingnode = self.dll.head
            while checkingnode is not None:
                if checkingnode.key == key:
                    checkingnode.value = value
                    
                checkingnode = checkingnode.next

        else:
            if self.dll.length < self.limit:
                self.dll.add_to_head(key, value)
                self.dic.update({key:value})
            else: 
                # self.dll.delete(self.dll.tail)
                self.dic.pop(self.dll.tail.key, None)
                self.dll.remove_from_tail()
                self.dll.add_to_head(key, value)
                self.dic.update({key:value})

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
        # DLL to store order
        # dict to store key value pairs
        # current size
        # limit
        self.max = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.storage = {}
    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache.
  """

    def get(self, key):
        # pull the value out of the dict using the key
        # update postition in the list
        # or return none

        # check if list has any elements
        if not self.list.head and not self.list.tail:
            return None
        # check if key in list
        current = self.find_node(key)

        # find value of key
        if current:
            self.list.move_to_front(current)

            for i in self.storage:
                if i == key:
                    return self.storage[i]
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
        '''
        - add to linked list
        - 
        '''
        # add pair to the cache - add to dict and add it  nodes/DLL
        # Mark as most recently used - put in the head of the DLL
        # if at max capacity, dump oldest - remove from tail of DLL
        # if already exists, overwrite value - update dict

        current = self.find_node(key)

        if current:
            for i in self.storage:
                if i == key:
                    self.storage[i] = value
            self.list.move_to_front(current)
        else:
            if self.size >= self.max:
                tail = self.list.remove_from_tail()
                self.storage.pop(tail)

            result = self.list.add_to_head(key)
            self.storage.update({key: value})
            self.size = self.list.length

            return result

    def find_node(self, key):
        current = self.list.head
        in_list = False
        while current and in_list == False:
            if current.value == key:
                in_list = True
            else:
                current = current.next
        if not in_list:
            current = None
        return current

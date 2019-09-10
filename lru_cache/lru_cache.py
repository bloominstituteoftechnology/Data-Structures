import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    self.max_num_nodes = limit
    self.current_nodes = 0
    self.cache = {}
    self.order = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    value = None
    if key in self.cache:
        
        node = self.cache[key]
        value = node[1]
        self.order.move_to_front(node)

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
    # is the key in our cache?
    # Case 3
    if key in self.cache:
        # overwrite the value in our DLL, self.order
        # move to the front, it's the most recently used
        node = self.cache[key]
        self.order.move_to_front(node)
        node.value = (key, value)

    else:
        # Case 2
        if self.current_nodes == self.max_num_nodes:
            del self.cache[self.order.tail.value[0]]# deletes key from cache
            self.order.remove_from_tail()
            self.current_nodes -= 1

        # Case 1
        self.order.add_to_head((key, value)) #most recently used value, add key/value pair (tuple)
        self.cache[key] = self.order.head
        self.current_nodes += 1
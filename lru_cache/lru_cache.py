import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.hash = {}
    self.storage = DoublyLinkedList(ListNode('temp'))

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """ 
  def get(self, key):

    if key in self.hash:
      ##
      value = self.hash[key]
      del self.hash[key]
      self.hash[key] = value
      ##

 
      ##move the current node to the end of the linked list + changed the arrows of the previous node to point to whatever the current node was pointing at
      curr_node = self.storage.head #Set the current node equal to the head of the storage linked list
      while curr_node.value is not key: #While the current node value does not equal the key value keep going to the next node until it matches
        curr_node = curr_node.next
      if curr_node is self.storage.head:
        self.storage.head = self.storage.head.next
      else: 
        self.storage.delete(curr_node)
      self.storage.move_to_end(curr_node)
      print('**************************')
      ##
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
    if self.storage.head.value == 'temp':
      self.storage.head = self.storage.head.next
    if len(self.hash) < self.limit or key in self.hash:
      if key not in self.hash:
        self.storage.add_to_tail(key)
      self.hash[key] = value
    else:
      oldKey = self.storage.head.value
      self.storage.head = self.storage.head.next
      self.storage.add_to_tail(key)
      del self.hash[oldKey]
      self.hash[key] = value
    
    
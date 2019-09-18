class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None


class LRUCache():
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.head = Node('Head')
    self.tail = Node('Tail')
    # Head --> Tail

    self.head.next = self.tail
    self.tail.prev = self.head
    self.map = {}
    self.size = 0

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    pass

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
    if key not in self.map:
      #insert
      node = Node(value)
      self.move_to_front(node)
      self.map[key] = node
      self.size += 1

  def move_to_front(self, node):
    #Head <--> Node1 <--> Node2 <--> Tail
    #New Node
    #Head <--> New Node <--> Node1 <--> Node2 <--> Tail
    node_1 = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = node_1
    node_1.prev = node

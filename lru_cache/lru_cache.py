class Node:
  def __init__(self, value, key=None):
    self.value = value
    self.prev = None
    self.next = None
    self.key = key
  
  def __str__(self):
    print (f"{self.value}")


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
    if key not in self.map:
      return False
    else:
      node = self.map[key]
      self.move_to_front(node)
      return node.value

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
      node = Node(value, key)
      self.move_to_front(node)
      self.map[key] = node
      self.size += 1

      #comparing length of nodes against the capacity
      if self.size > self.limit:
        del self.map[self.tail.prev.key]
        self.remove(self.tail.prev)
        self.size -= 1

    else:
      node = self.map[key]
      node.value = value
      self.remove(node)
      self.move_to_front(node)

  def move_to_front(self, node):
    #Head <--> Node1 <--> Node2 <--> Tail
    #New Node
    #Head <--> New Node <--> Node1 <--> Node2 <--> Tail
    node_1 = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = node_1
    node_1.prev = node

  def remove(self, node):
    #Head <--> Node1 <--> <--> Node To Delete <--> Node2 <--> Tail
    #Head <--> Node1 <--> Node2 <--> Tail
    node_1 = node.prev
    node_2 = node.next

    #Point two nodes to each other
    node_1.next = node_2
    node_2.prev = node_1
    node.next = None
    node.prev = None

  def _print_cache(self):
    if self.size != 0:
      print (f"{self.head.value} {self.head.next.value} {self.tail.prev.value} {self.tail.value}")

cache = LRUCache()
cache.set(2, 2)
cache.set(1, 3)

cache._print_cache()
print(cache.map)
print(cache.get(2))
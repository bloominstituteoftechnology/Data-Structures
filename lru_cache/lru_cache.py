from doubly_linked_list import DoublyLinkedList
class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.lru_cache = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if self.lru_cache.length == 0:
      return None
    node = self.lru_cache.head
    while (node):
      if key in node.value:
        item = node.value
        self.lru_cache.delete(node)
        self.lru_cache.add_to_tail(item)
        return [*item.values()][0]
      node = node.next
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
    item = dict()
    item[key] = value
    self.lru_cache.delete(self.get_node(key))
    if self.lru_cache.length == self.limit:
      self.lru_cache.remove_from_head()
    self.lru_cache.add_to_tail(item)

  def get_node(self, key):
    if self.lru_cache.length == 0:
      return None
    node = self.lru_cache.head
    while (node):
      if key in node.value:
        return node
      node = node.next
    return None

cache = LRUCache(3)

cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
cache.set('item2', 'z')
res = cache.get('item1')

pass

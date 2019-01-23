class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.hash = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.hash:
      value = self.hash[key]
      del self.hash[key]
      self.hash[key] = value
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
    if len(self.hash) < self.limit or key in self.hash:
      self.hash[key] = value
    else: 
      oldKey = list(self.hash)[0]
      del self.hash[oldKey]
      self.hash[key] = value
    
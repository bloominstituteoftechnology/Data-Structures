class LRUCache:
  def __init__(self, limit=10):
      self.cache = []
      self.limit = limit

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def index_of(self, key):
      matches = [i for i, (k, v) in enumerate(self.cache) if k == key]
      return matches[0] if len(matches) else None

  def get(self, key):
      i = self.index_of(key)

      if i:
          self.cache = [self.cache.pop(i)] + self.cache
          return self.cache[0][1]
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
      i = self.index_of(key)

      if i:
          self.cache[i] = (key, value)
      else:
          self.cache = [(key, value)] + self.cache

          if self.limit < len(self.cache):
              self.cache.pop(-1)

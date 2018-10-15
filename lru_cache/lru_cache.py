import collections

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.cache = collections.OrderedDict()

  def get(self, key):
    # Attempt to fetch the key-value pair from the cache
    try:
      value = self.cache.get(key)
      # Move the key-value pair to the front of the cache to maintain ordering
      self.cache.move_to_end(key, last=True)
      return value
    except KeyError:
      return None

  def set(self, key, value):
    # Check to see if the key is already in the cache
    if not self.cache.get(key):
      # Check to see if the cache is holding the maximum number of keys
      if len(self.cache) >= self.limit:
        # Remove the least-recently accessed key
        self.cache.popitem(last=False)
    # Add the key-value pair to the cache
    self.cache[key] = value
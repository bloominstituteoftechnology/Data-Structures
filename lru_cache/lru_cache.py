class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = {}

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache.
  """

    def get(self, key):
        for k in self.cache:
            if k == key:
                return self.cache[key]

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
        # if key exists overwrite it
        if self.cache.get(key):
            self.cache[key] = value

        # add key value pair
        if len(self.cache) < self.limit:
            self.cache[key] = value


lru_cache = LRUCache(3)
lru_cache.set('hello', 'world')
lru_cache.set('mellon', 'jam')
lru_cache.set('great', 'peace')
lru_cache.set('mellon', 'eyes')
print(lru_cache.cache)
print(len(lru_cache.cache))

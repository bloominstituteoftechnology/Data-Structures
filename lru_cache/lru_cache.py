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
                # get value
                value = self.cache[k]
                # remove key value
                self.cache.pop(k)
                # reinset value as most recently used
                self.set(k, value)
                # return value
                return self.cache[k]

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
        popped = None
        # if key exists overwrite it
        if self.cache.get(key):
            self.cache[key] = value

        # add key value pair
        elif self.limit == len(self.cache):
            for i, k in enumerate(self.cache):
                # if the last item in dict
                if i == 0:
                    popped = k
                    self.cache.pop(popped)
                    self.cache[key] = value
                    break
        else:
            self.cache[key] = value

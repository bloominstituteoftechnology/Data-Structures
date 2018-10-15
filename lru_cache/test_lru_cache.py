import unittest
from lru_cache import LRUCache

class LRUCacheTests(unittest.TestCase):
  def setUp(self):
    self.cache = LRUCache(3)

  def test_lru_cache_overwrites_appropriately(self):
    self.cache.set('item1', 'a')
    self.cache.set('item2', 'b')
    self.cache.set('item3', 'c')

    self.cache.set('item2', 'z')

    self.assertEqual(self.cache.get('item1'), 'a')
    self.assertEqual(self.cache.get('item2'), 'z')

  def test_lru_cache_insertion_and_retrieval(self):
    self.cache.set('item1', 'a')
    self.cache.set('item2', 'b')
    self.cache.set('item3', 'c')

    self.assertEqual(self.cache.get('item1'), 'a')
    self.cache.set('item4', 'd')

    self.assertEqual(self.cache.get('item1'), 'a')
    self.assertEqual(self.cache.get('item3'), 'c')
    self.assertEqual(self.cache.get('item4'), 'd')
    self.assertIsNone(self.cache.get('item2'))

  def test_lru_cache_nonexistent_retrieval(self):
    self.assertIsNone(self.cache.get('nonexistent'))


if __name__ == '__main__':
  unittest.main()
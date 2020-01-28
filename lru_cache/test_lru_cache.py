import unittest
from lru_cache import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    def test_cache_overwrite_appropriately(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')

        self.cache.set('item2', 'z')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item2'), 'z')

    def test_cache_insertion_and_retrieval(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.cache.set('item4', 'd')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item3'), 'c')
        self.assertEqual(self.cache.get('item4'), 'd')
        self.assertIsNone(self.cache.get('item2'))

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent'))

    def test_cache_max_size(self):
        self.assertEqual(self.cache.limit, 3)
        self.assertEqual(len(self.cache), 0)
        self.cache.set('a', "a")
        self.assertEqual(len(self.cache), 1)
        self.cache.set('b', "z")
        self.assertEqual(len(self.cache), 2)
        self.cache.set('b', "b")
        self.assertEqual(len(self.cache), 2)
        self.cache.set('b', "b")
        self.assertEqual(len(self.cache), 2)

        self.assertEqual(self.cache.limit, 3)

        self.cache.set('c', "c")
        self.assertEqual(len(self.cache), 3)
        self.cache.set('d', "d")
        self.assertEqual(len(self.cache), 3)
        self.cache.set('e', "e")
        self.assertEqual(len(self.cache), 3)

if __name__ == '__main__':
    unittest.main()

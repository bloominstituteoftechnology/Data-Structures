import unittest
from unittest.mock import MagicMock
from heap import Heap

class HeapTests(unittest.TestCase):
  print('\n---NEW TEST RUN---')
  def setUp(self):
    self.heap = Heap()

  def test_heap_insert_works(self):
    print('\nTest insert:')
    self.heap.insert(6)
    self.heap.insert(8)
    self.heap.insert(10)
    self.heap.insert(9)
    self.heap.insert(1)
    self.heap.insert(9)
    self.heap.insert(9)
    self.heap.insert(5) 
    self.assertEqual(self.heap.storage, [10, 9, 9, 6, 1, 8, 9, 5])

  def test_get_max_works(self):
    print('\nTest get max: ')
    self.heap.insert(6)
    self.heap.insert(8)
    self.heap.insert(10)
    self.heap.insert(9)
    self.heap.insert(1)
    self.heap.insert(9)
    self.heap.insert(9)
    self.heap.insert(5)
    self.assertEqual(self.heap.get_size(), 8)
    self.assertEqual(self.heap.get_max(), 10)

  def test_get_max_after_delete(self):
    print('\nTest get max after delete: ')
    self.heap.insert(6)
    self.heap.insert(8)
    self.heap.insert(10)
    self.heap.insert(9)
    self.heap.insert(1)
    self.heap.insert(9)
    self.heap.insert(9)
    self.heap.insert(5)
    self.heap.delete()
    self.assertEqual(self.heap.get_max(), 9)
    self.heap.delete()
    self.assertEqual(self.heap.get_max(), 9)
    self.heap.delete()
    self.assertEqual(self.heap.get_max(), 9)
    self.heap.delete()
    self.assertEqual(self.heap.get_max(), 8)
    self.heap.delete()
    self.assertEqual(self.heap.get_max(), 6)

  def test_delete_elements_in_order(self):
    print('\nTest delete elements in order: ')
    self.heap.insert(6)
    self.heap.insert(7)
    self.heap.insert(5)
    self.heap.insert(8)
    self.heap.insert(10)
    self.heap.insert(1)
    self.heap.insert(2)
    self.heap.insert(5)

    descending_order = []

    while self.heap.get_size() > 0:
      descending_order.append(self.heap.delete())

    self.assertEqual(descending_order, [10, 8, 7, 6, 5, 5, 2, 1])

  def test_bubble_up_was_called(self):
    print('\nTest bubble up was called')
    self.heap._bubble_up = MagicMock()
    self.heap.insert(5)
    self.assertTrue(self.heap._bubble_up.called)

  def test_sift_down_was_called(self):
    self.heap._sift_down = MagicMock()
    self.heap.insert(10)
    self.heap.insert(11)
    self.heap.delete()
    self.assertTrue(self.heap._sift_down.called)

if __name__ == '__main__':
  unittest.main()
import unittest
from linked_list import LinkedList

class LinkedListTests(unittest.TestCase):
  def setUp(self):
    self.list = LinkedList()

  def test_add_to_tail(self):
    self.list.add_to_tail(1)
    self.assertEqual(self.list.tail.value, 1)
    self.assertEqual(self.list.head.value, 1)
    self.list.add_to_tail(2)
    self.assertEqual(self.list.tail.value, 2)
    self.assertEqual(self.list.head.value, 1)

  def test_contains(self):
    self.list.add_to_tail(1)
    self.list.add_to_tail(2)
    self.list.add_to_tail(5)
    self.list.add_to_tail(10)
    self.assertTrue(self.list.contains(10))
    self.assertTrue(self.list.contains(2))
    self.assertFalse(self.list.contains(1000))

  def test_remove_head(self):
    self.list.add_to_tail(10)
    self.list.add_to_tail(20)
    self.assertEqual(self.list.remove_head(), 10)
    self.assertFalse(self.list.contains(10))
    self.assertEqual(self.list.remove_head(), 20)
    self.assertFalse(self.list.contains(20))

    self.list.add_to_tail(10)    
    self.assertEqual(self.list.remove_head(), 10)    
    self.assertIsNone(self.list.head)
    self.assertIsNone(self.list.tail)
    self.assertIsNone(self.list.remove_head())

  def test_get_max(self):
    self.assertIsNone(self.list.get_max())
    self.list.add_to_tail(100)
    self.assertEqual(self.list.get_max(), 100)
    self.list.add_to_tail(55)
    self.assertEqual(self.list.get_max(), 100)
    self.list.add_to_tail(101)
    self.assertEqual(self.list.get_max(), 101)

if __name__ == '__main__':
  unittest.main()

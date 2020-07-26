import unittest

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
    
    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def contains(self, value):
        if not self.head:
            return False
        
        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None
        
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        
        return cur_node

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_get_max(self):
        self.assertIsNone(self.list.get_max())
        self.list.add_to_tail(100)
        self.assertEqual(self.list.get_max(), 100)
        self.list.add_to_tail(55)
        self.assertEqual(self.list.get_max(), 100)
        self.list.add_to_tail(101)
        self.assertEqual(self.list.get_max(), 101)

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

if __name__ == '__main__':
    unittest.main()
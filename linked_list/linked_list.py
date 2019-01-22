"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
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

  def add_to_tail(self, value):
      node = Node(value)
      if self.tail is None:
        self.head = node
      else:
        self.tail.set_next(node)
      self.tail = node

  def remove_head(self):
      if self.head is not None:
          old_head = self.head
          new_head = self.head.get_next()
          self.head = new_head
          return old_head.value

  def contains(self, value):
      current_node = self.head
      print(current_node.value)
      while True:
          if current_node is None:
              return False
          elif current_node.value == value:
              return True
          else:
              current_node = current_node.next_node

  def get_max(self):
      if self.head is not None:
          max_node = self.head
          if max_node.next_node is not None:
              next_node = max_node.get_next()
              while True:
                  if max_node.get_value() < next_node.get_value():
                      max_node = next_node
                  else:
                      return max_node.get_value()
          else:
              return max_node.get_value()
      else:
          return None



ll = LinkedList()

ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)

print(ll.head.value)

print(ll.remove_head())

print(ll.head.value)
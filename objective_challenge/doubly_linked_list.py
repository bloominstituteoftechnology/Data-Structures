"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.__len__() == 0:   # when the idiot wants to do this to a null dll
      node = ListNode(value)
      self.head = node
      self.tail = node
      self.length = 1
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1

  def remove_from_head(self):
    if self.__len__() > 0:
      ret = self.head.value
      self.head.delete()
      self.length -= 1
      if self.length == 0:  # no nodes left
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next
      return ret

  def add_to_tail(self, value):
    if self.__len__() == 0:   # when the idiot wants to do this to a null dll
      node = ListNode(value)
      self.head = node
      self.tail = node
      self.length = 1
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.length += 1

  def remove_from_tail(self):
    if self.__len__() > 0:
      ret = self.tail.value
      self.tail.delete()
      self.length -= 1
      if self.length == 0:  # no nodes left
        self.head = None
        self.tail = None
      else:
        self.tail = self.tail.prev
      return ret

  def move_to_front(self, node):
    dll_len = self.__len__()
    if dll_len <= 1:
      return
    if node == self.head:
      return
    if dll_len == 2:    # handle special when swapping head & tail
      self.head = node
      self.tail = node.prev
      self.head.prev= None
      self.tail.next = None
      self.head.next = self.tail
      self.tail.prev = self.head
      return
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    node.prev = None
    node.next = self.head
    self.head.prev = node
    self.head = node

  def move_to_end(self, node):
    dll_len = self.__len__()
    if dll_len <= 1:
      return
    if node == self.tail:
      return
    if dll_len == 2:    # handle special when swapping head & tail
      self.tail = node
      self.head = node.next
      self.head.prev= None
      self.tail.next = None
      self.head.next = self.tail
      self.tail.prev = self.head
      return
    if node.prev:
      node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    node.next = None
    node.prev = self.tail
    self.tail.next = node
    self.tail = node

  def delete(self, node):
    if node:
      if not node.prev:
        self.remove_from_head()
      elif not node.next:
        self.remove_from_tail()
      else:
        node.delete()
        self.length -= 1

  def get_max(self):
    max_val = self.head.value
    next_node = self.head.next
    while(next_node):
      if next_node.value > max_val:
        max_val = next_node.value
      next_node = next_node.next
    return max_val

node = ListNode(1)
dll = DoublyLinkedList(node)

dll.add_to_head(2)
dll.add_to_tail(3)
dll.add_to_head(4)
dll.add_to_tail(5)

i = dll.get_max()

dll.move_to_front(dll.tail.prev)
dll.move_to_end(dll.head.next)

dll.remove_from_head()
dll.remove_from_tail()

dll.delete(dll.head.next)
dll.delete(dll.head.next)
dll.delete(dll.tail)
#dll1 = DoublyLinkedList()
#dll1.add_to_head(2)
pass

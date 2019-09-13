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
    new_node = ListNode(value)
    self.length += 1
    if not self.tail and not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remove_from_head(self):

    # pass
    if self.head is None and self.tail is None:
      return None
    elif self.head is self.tail:
      return_value = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return return_value.value
    else:
      return_value = self.head
      self.head = self.head.next
      self.head.prev = None
      self.delete(self.head)
      self.length -= 1
      return return_value.value

  def add_to_tail(self, value):
    # pass
    new_tail = ListNode(value)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_tail
      self.tail = new_tail
    else:
      new_tail.prev = self.tail
      self.tail.next = new_tail
      self.tail = new_tail
      new_tail.next = None


  def remove_from_tail(self):
    # pass
    if not self.tail:
          return None
    elif self.tail is self.head:
          return_value = self.tail.value
          self.tail = None
          self.head = None
          self.length -= 1
          return return_value
    else:
          return_value = self.tail.value
          self.tail = self.tail.prev
          self.tail.next = None
          self.delete(self.tail)
          self.length -= 1
          return return_value.value

  def move_to_front(self, node):
    # pass
      if node == self.head:
            return self.head
      else:
            self.add_to_head(node.value)
            self.length -= 1
            node.delete()

  def move_to_end(self, node):
    # pass
    if node == self.head:
        self.head = node.next

    original_tail = self.tail
    self.tail = node

    if node.prev is not None:
      node = node.next

    if node.next is not None:
      node.next = node.prev

    self.tail.prev = original_tail
    original_tail.next = self.tail

  def delete(self, node):
    # pass
    if node is self.head and node is self.tail:
          node.delete()
          self.head = None
          self.tail = None
          self.length = 0
          return
    elif node == self.head:
          self.head = self.head.next
          node.delete()
    elif node == self.tail:
          self.tail = self.tail.prev
          node.delete()
    node.delete()
    self.length -= 1

  def get_max(self):
    # pass
    current_node = self.head
    greatest = 1
    while current_node != self.tail:
      if current_node.value > current_node.next.value:
        greatest = current_node.value
      else:
        greatest = current_node.next.value
      current_node = current_node.next
    return greatest

  # def get_middle(self):
  #   current_node = self.head
  #   length = 0
  #   middle = current_node
  #   while current_node.next != None:
  #     length++
  #     if length%2 == 0:
  #           middle = 


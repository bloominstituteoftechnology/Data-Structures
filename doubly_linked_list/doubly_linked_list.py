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

  def add_to_head(self, value):
    if self.head is not None:
      self.head.insert_before(value)
      self.head = self.head.prev
    else:
      self.head = ListNode(value)
      self.tail = self.head

  def remove_from_head(self):
    if self.head is not None:
      current_head = self.head
      self.head.delete()
      return current_head.value

  def add_to_tail(self, value):
    if self.tail is not None:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      self.head = ListNode(value)
      self.tail = self.head

  def remove_from_tail(self):
    if self.tail is not None:
      current_tail = self.tail
      self.tail.delete()
      return current_tail.value

  def move_to_front(self, node):
    current_node = node.value
    node.delete()
    self.add_to_head(current_node)

  def move_to_end(self, node):
    current_node = node.value
    node.delete()
    self.add_to_tail(current_node)

  def delete(self, node):
    node.delete()
    
  def get_max(self):
    if self.head is not None and self.head != self.tail: # Personally, I feel like get_max should return the value of the single node... Oh well...
      current_node = self.head
      maximum = current_node
      while True:
        if current_node.value > maximum.value:
          maximum = current_node
        if current_node.next == None:
          return maximum.value
        else:
          current_node = current_node.next
    else:
      return None
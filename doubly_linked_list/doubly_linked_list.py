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
    new_node = ListNode(value)
    new_node.next = self.head
    self.head = new_node
    if self.head is None:
      self.tail = new_node

  def remove_from_head(self):
    if self.head:
      prev_head = self.head
      self.head = prev_head.next
      return prev_head.value

  def add_to_tail(self, value):
    new_node = ListNode(value)
    new_node.prev = self.tail

    if self.tail is None:
      self.head = new_node
      self.tail = new_node
      return
    self.tail.insert_after(value)
    self.tail = self.tail.next 

  def remove_from_tail(self):
    if self.tail:
      prev_tail = self.tail
      self.tail = prev_tail.next
      return prev_tail.value

  def move_to_front(self, node):
    if node.next is not None:
      node.next.prev = node.prev
    if node.prev is not None:
      node.prev.next = node.next
    self.head.prev = node
    node.next = self.head
    node.prev = None
    self.head = node
    
  def move_to_end(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node 

  def delete(self, node):
    node.delete()

  def get_max(self):  
    max = None  
    curr_node = self.head
    while curr_node is not None:  
      if max is None or curr_node.value > max:  
        max = curr_node.value  
      curr_node = curr_node.next  
    return max  
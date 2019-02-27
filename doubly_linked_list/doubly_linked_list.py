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
    current_head= self.head
    if current_head is None:
      self.head= ListNode(value)
    else:
      current_head.insert_before(value)
      self.head= current_head.prev

  def remove_from_head(self):
    current_head = self.head
    if not current_head:
      return None
    else:
      self.head = current_head.next  # if doesn't exist will be None
      try:
        current_head.next.prev = None
      except:
        pass
      return current_head.value

  def add_to_tail(self, value):
    current_tail= self.tail
    if current_tail is None:
      self.tail= ListNode(value)
    else:
      current_tail.insert_after(value)
      self.tail= current_tail.next
  def remove_from_tail(self):
    current_tail=self.tail
    if not current_tail:
      return None
    else:
      self.tail= current_tail.prev
      try:
        current_tail.prev.next=None
      except:
        pass
      return current_tail.value

  def move_to_front(self, node):
    if self.head is not node:
      if node.next and node.prev:
        node.prev.next = node.next
        node.next.prev = node.prev
      elif not node.next:  
        node.prev.next = None

      current_head = self.head
      self.head = node
      node.next = current_head
      current_head.prev = node

  def move_to_end(self, node):
      if self.tail is not node:
          if node.next and node.prev:  
              node.prev.next = node.next
              node.next.prev = node.prev
          else:  
              node.next.prev = None
          current_tail = self.tail
          self.tail = node
          node.prev = current_tail
          current_tail.next = node

  def delete(self, node):
      node.delete

  def get_max(self):
      max = 0
      pointer = self.head
      while pointer:
          if pointer.value > max:
              max = pointer.value
          pointer = pointer.next
      return max

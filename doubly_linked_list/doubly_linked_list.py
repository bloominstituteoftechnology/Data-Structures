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
    if self.head is None:
      self.head = self.tail = ListNode(value)
      return
    else:
      self.head.insert_before(value)
      self.head = self.head.prev

  def remove_from_head(self):
    old_head = self.head.value
    new_head = self.head.next
    self.head.delete()
    self.head = new_head
    return old_head

  def add_to_tail(self, value):
    if self.tail is None:
      self.tail = self.head = ListNode(value)
      return
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

  def remove_from_tail(self):
    old_tail = self.tail.value
    new_tail = self.tail.prev
    self.tail.delete()
    self.tail = new_tail
    return old_tail

  def move_to_front(self, node):
    if node is None:
      return
    else:
      next_up = self.head
      if next_up:
        if next_up.value is not node.value:
          next_up = next_up.next
        else:
          next_up.delete()
      self.add_to_head(node.value)


  def move_to_end(self, node):
    if node is None:
      return
    else:
      last = self.tail
      if last:
        if last.value is not node.value:
          last = last.prev
        else:
          last.delete()
      self.add_to_tail(node.value)

  def delete(self, node):
    if node.next:
      node.next.prev = node.prev
    if node.prev:
      node.prev.next = node.next
    node.delete()

    
  def get_max(self):
    current = self.head
    if current is None or self.tail is None:
      return None
    elif self.head ==  self.tail:
      return None
    max_node = current
    next_up = current.next
    while next_up:
      if next_up.value > max_node.value:
        max_node = next_up
      else:
        next_up = next_up.next
    return max_node.value

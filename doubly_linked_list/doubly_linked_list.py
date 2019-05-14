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
    if self.length == 0:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1


  def remove_from_head(self):
    old_head = self.head
    if self.length == 0:
      return 
    else:
      self.head.delete()
      self.head = self.head.next
      self.tail = self.tail if self.head is not None else None
      self.length -= 1
    return old_head.value if old_head is not None else None

  def add_to_tail(self, value):
    if self.tail:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    else:
      new_head_tail = ListNode(value)
      self.head = new_head_tail
      self.tail = new_head_tail
    self.length += 1

      
  def remove_from_tail(self):
    old_tail = self.tail
    if self.length == 0:
      return 
    else:
      self.tail.delete()
      self.tail = self.tail.prev
      self.head = self.head if self.tail is not None else None
      self.length -= 1
    return old_tail.value if old_tail is not None else None

  def move_to_front(self, node):
    if self.length > 1 and node != self.head:
      current_node = node
      node.delete()
      self.head.insert_before(current_node.value)
      self.head = self.head.prev
      self.tail = self.tail if node != self.tail else current_node.prev

  def move_to_end(self, node):
    if self.length > 1 and node != self.tail:
      current_node = node
      node.delete()
      self.tail.insert_after(current_node.value)
      self.tail = self.tail.next
      self.head = self.head if node != self.head else current_node.next

  def delete(self, node):
    current_node = node
    node.delete()
    self.head = self.head if node != self.head else current_node.next
    self.tail = self.tail if node != self.tail else current_node.prev
    self.length -= 1
    
  def get_max(self):
    current = self.head
    max_value = self.head.value
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.next
    return max_value

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
    if self.head:
      self.head.insert_before(value)
      curr_head = self.head
      self.head = ListNode(value, None, curr_head)
    else:
      new_head = ListNode(value, None, None) 
      self.head = new_head
      self.tail = new_head
    self.length += 1

  def remove_from_head(self):
    # MY OWN CODE!
    # if self.length == 0:
    #   pass
    # elif self.length == 1:
    #   curr_head = self.head
    #   self.head = None
    #   self.tail = None
    #   self.length -= 1
    #   return curr_head.value
    # elif self.length > 1:
    #   curr_head = self.head
    #   self.head = curr_head.next
    #   curr_head.delete()
    #   self.length -= 1
    #   return curr_head.value
    # IN CLASS CODE!
    removed = self.head.value
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.head = self.head.next
      self.head.prev.delete()
      self.length -= 1
    return removed


  def add_to_tail(self, value):
    # if already an existing tail...
    if self.tail:
      curr_tail = self.tail
      # point current tail's next to new tail
      self.tail.insert_after(value)
      # set new tail, with prev set to previous tail
      self.tail = ListNode(value, curr_tail, None)
    # else if no node, set new node as head and tail
    else:
      new_tail = ListNode(value, None, None) 
      self.head = new_tail
      self.tail = new_tail
    # add to list length
    self.length += 1

  def remove_from_tail(self):
    removed = self.tail.value
    if self.head == self.tail:
      self.tail = None
      self.head = None
      self.length = 0
    else:
      self.tail = self.tail.prev
      self.tail.next.delete()
      self.length -= 1
    return removed

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass

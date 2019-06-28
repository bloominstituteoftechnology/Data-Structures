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

    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev

    self.length += 1  


  def remove_from_head(self):
    removed_node = self.head.value

    if self.head == self.tail:
      self.head == None
      self.tail == None
    else:
      self.head = self.head.next
      self.head.prev.delete()  

    self.length -= 1
    return removed_node

  def add_to_tail(self, value):
    new_tail = ListNode(value)

    if self.head == None and self.tail == None:
      self.head == new_tail
      self.tail == new_tail
    else:
      new_tail.prev = self.tail
      self.tail.next  = new_tail
      self.tail = new_tail

    self.length += 1  

  def remove_from_tail(self):
    
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next.delete()  

  def move_to_front(self, node):
    #see if node is already first
    #

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    if self.head == None:
      return None
    else:  
      current_max = self.head.value
      current_node = self.head
      while


    return current_max

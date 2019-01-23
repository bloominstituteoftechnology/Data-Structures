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
    node = ListNode(value, self)
    node.next = self.head
    self.head = node
    if self.head == None:
      self.tail = node
    pass


  def remove_from_head(self):
    if self.head == None and self.tail == None:
      return None

    if self.head.next != None:
      return_val = self.head.value
      self.head = self.head.next
      self.tail = self.head.value
      # print(self)
      return return_val
    else:
      return_val = self.head.value
      self.head = None
      self.tail = None
      # print(self)
      return return_val
    pass

  def add_to_tail(self, value):
    node = ListNode(value, self)
    node.next = self.tail
    self.tail = node
    if self.head == None:
      self.head = node
    pass

  def remove_from_tail(self):
    if self.head == None and self.tail == None:
      return None
    temp = self.tail
    if self.tail.prev is not None:
      temp = self.tail
      self.tail.delete()
      self.tail = temp.prev
      return temp.value
    else:
      temp = self.tail
      self.tail.delete()
      return temp.value

  def move_to_front(self, node):
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.head.prev = node
    node.prev = None
    node.next = self.head
    self.head = node

  def move_to_end(self, node):
    #previous.next should equal next.previous
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node

  def delete(self, node):
    pass
    
  def get_max(self):
    current = self.tail

    if current == None:
      return None
    else:
      maximum = self.tail.value
      while current != None:
        if current.value > maximum:
          maximum = current.value
        current = current.next
        print(maximum)
      return maximum

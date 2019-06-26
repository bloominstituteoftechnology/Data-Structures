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

    if self.head == None:
      node = ListNode(value)
      self.head = node
      self.tail = node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev

    self.length += 1

  def remove_from_head(self):
    if self.head is not None:
      val = self.head.value

      if self.head != self.tail:
        self.head = self.head.next
        self.head.prev.delete()
      else:
        self.head.delete()
        self.head = None
        self.tail = None

      self.length -= 1
      return val

  def add_to_tail(self, value):
    if self.tail == None:
      node = ListNode(value)
      self.head = node
      self.tail = node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

    self.length += 1

  def remove_from_tail(self):
    if self.tail is not None:

      val = self.tail.value

      if self.tail != self.head:
        self.tail = self.tail.prev
        self.tail.next.delete()
      else:
        self.tail.delete()
        self.head = None
        self.tail = None

      self.length -= 1
      return val

  def move_to_front(self, node):
    # remove 'node'
    # add 'node' to head
    value = node.value # save the value first

    if node is self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
    self.add_to_head(value)
    


  def move_to_end(self, node):
    value = node.value

    if node is self.head:
      self.remove_from_head()
    else:
      node.delete()
      self.length -= 1
    self.add_to_tail(value)

  def delete(self, node):
    if node == self.head:
      self.head = self.head.next

    if node == self.tail:
      self.tail = self.tail.prev

    node.delete()
    self.length -= 1
    
  def get_max(self):
    max = 0

    if self.head is not None:
      max = self.head.value
      node = self.head

      while node.next is not None:
        if node.value > max:
          max = node.value

        node = node.next
      
      if node.value > max:
        max = node.value

    return max

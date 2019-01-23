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
## ListNode Methods
# insert_after(value)
# insert_before(value)
# delete()
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    node = ListNode(value)

    if self.head != None and self.tail != None:
      self.head.insert_before(node)
      self.head = node

    else:
      self.head = node
      self.tail = node

  def remove_from_head(self):
    if self.head is None and self.tail is None:
      retval = None
    elif self.head == self.tail:
      retval = self.head.value
      self.head = None
      self.tail = None
    else:
      retval = self.head.value
      new_head = self.head.next
      self.head.delete()
      self.head = new_head
    return retval

  def add_to_tail(self, value):
    node = ListNode(value)
    if self.head is not None and self.tail is not None:
      self.tail.insert_after(node)
      self.tail = node
    
    else:
      self.head = node
      self.tail = node

  def remove_from_tail(self):
    if self.head is None and self.tail is None:
      retval = None
    elif self.head == self.tail:
      retval = self.tail.value
      self.head = None
      self.tail = None
    else:
      retval = self.tail.value
      new_tail = self.tail.prev
      self.tail.delete()
      self.tail = new_tail
    return retval

  def move_to_front(self, node):
    if self.head == None:
      return 'List Empty'
    else:
      curr_node = self.head
      while True:
        ## if curr_node matches passed in node
        if curr_node == node:
          # self.add_to_head(curr_node.value)
          self.head.insert_before(node)
          # delete curr_node
          curr_node.delete()
        ## else:
        else:
          # curr_node = curr_node.next
          curr_node = curr_node.next



  def move_to_end(self, node):
    if self.head == None:
      return 'list empty'
    else:
      curr_node = self.head
      while True:
        ## if curr_node matches passed in node
        if curr_node == node:
          self.head.insert_after(node)
          curr_node.delete()
        else:
          curr_node = curr_node.next

  def delete(self, node):
    if self.head == None:
      return 'list empty'
    else:
      curr_node = self.head
      while True:
        if curr_node == node:
          return curr_node.delete()
        else:
          curr_node = curr_node.next
    
  def get_max(self):
    if self.head == None:
      return 'list empty'
    else:
      curr_node = self.head
      curr_highest = self.head
      while True:
        if curr_node == None:
          return curr_highest.value
        if curr_node.next.value > curr_highest.value:
          curr_highest = curr_node.next
          curr_node = curr_node.next
        else:
          curr_node = curr_node.next

# DLL = DoublyLinkedList()
# DLL.add_to_head(5)
# DLL.add_to_head(4)
# DLL.add_to_head(16)
# print(DLL.remove_from_head())

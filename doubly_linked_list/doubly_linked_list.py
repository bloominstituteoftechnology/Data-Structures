"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def __repr__(self):
    return "Value: {}, ".format(self.value if self.value else None) + "Prev: {}, ".format(self.prev.value if self.prev else None) + "Next: {} \n".format(self.next.value if self.next else None)

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is pointing to."""
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
  
  def __repr__(self):
    return f"Head: {self.head} \n Tail: {self.tail} \n Length: {self.length}"

  def __len__(self):
    return self.length

  """Replaces the head of the list with a new value that is passed in."""
  def add_to_head(self, value):
    if self.length == 0:
      self.head = ListNode(value)
      self.tail = self.head
      self.length = 1
    else:
      self.head.prev = ListNode(value, None, self.head)
      self.head = self.head.prev
      self.length += 1

  """Replaces the tail of the list with a new value that is passed in."""
  def remove_from_head(self):
    if self.length == 0:
      return None
    current_head = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
      self.length -=1
      return current_head.value
    else:
      self.head = self.head.next
      self.head.prev = None
      self.length -=1
      return current_head.value

  """Removes the head node and returns the value stored in it."""
  def add_to_tail(self, value):
    if self.length == 0:
      self.tail = ListNode(value)
      self.head = self.tail
      self.length = 1
    else:
      self.tail.next = ListNode(value, self.tail, None)
      self.tail = self.tail.next
      self.length += 1

  """Removes the tail node and returns the value stored in it"""
  def remove_from_tail(self):
    if self.length == 0:
      return None
    current_tail = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
      self.length -= 1
      return current_tail.value
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      self.length -= 1
      return current_tail.value

  """Takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down."""
  def move_to_head(self, node):
    if node is self.head:
      return node
    if node is self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -= 1
    self.add_to_head(node.value)
    

  """Takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up."""
  def move_to_tail(self, node):
    if node is self.tail:
      return node
    if node is self.head:
      self.remove_from_head()
    else:
      node.delete()
      self.length -= 1
    self.add_to_tail(node.value)

  """Takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards."""
  def delete(self, node):
    if self.head == self.tail:
      self.remove_from_head()
    elif node is self.head:
      self.remove_from_head()
    elif node is self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      return node.value
    
    
  """Returns the maximum value in the list."""
  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.value
    current = self.head
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.next
    return max_value

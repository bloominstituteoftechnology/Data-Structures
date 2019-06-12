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
    # wrap the value in a node 
    
    # check if we're in an empty list state
    if not self.head and not self.tail:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    # add new value as new head
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1


  def remove_from_head(self):
    
    #set head value to none if there is no value
    #delete value if there are more than one value
    value = self.head.value
    if self.head is self.tail:
      self.head = None
      self.tail = None
    # elif len(self) == 0:
    #   self.head = None
    #   self.tail = None
    #   return value
    else:
      self.head.delete()
    self.length = self.length - 1
    
    return value
      
    
   

    

  def add_to_tail(self, value):
    # wrap the value in a node 
    
    # check if we're in an empty list state
    if not self.head and not self.tail:
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    # add new value as new head
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length += 1
   

  def remove_from_tail(self):
    # if not self.tail:
    #   self.tail == None
    # else:
    #   self.tail.delete()
    #   self.tail -= 1
    value = self.tail.value
    if self.tail is self.head:
      self.head = None
      self.tail = None
    # elif self.head.value == self.tail.value:
    #   self.head = None
    #   self.tail = None
    else:
      self.tail.delete()
    self.length = self.length - 1
    
    return value
    

  def move_to_front(self, node):
    #add node to head of the list
    #if node is head, return none
    #if node is tail, delete tail
    if node == self.head:
      return None
    
    self.add_to_head(node.value)
    if node == self.tail:
      # self.tail.delete()
      self.tail = self.tail.next
      node.delete()
    self.length = self.length -1

      
  def move_to_end(self, node):
    #checks if node is already a tail
    if node == self.tail:
      return None
    # adds node to the end as tail
    self.add_to_tail(node.value)
    #checks node if it is a head, move it to the next value and delete node
    if node == self.head:
      self.head = self.head.next
      node.delete()
    self.length = self.length - 1

  def delete(self, node):
    pass
    
    
  def get_max(self):
    pass

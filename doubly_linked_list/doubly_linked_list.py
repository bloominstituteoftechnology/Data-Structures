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
  def insert_after(self, value):  # O(1)
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):  # O(1)
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):  # O(1)
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

  def add_to_head(self, value):  # O(1)
    
    # Create new node
    # Check if head exists, 
      # If no, set the head and tail to be the new node
      # If yes, set the tail of the new node to be the old head and set the head to be the new node
    
    new_node = ListNode(value)
    
    if self.head is None:
      self.head = new_node
      self.tail = new_node
  
    new_node.next = self.head
    self.head = new_node

  def remove_from_head(self):  # O(1)
    
    # If the head exists...
      # Set the head to be the old head's next
      # Set the head's previous to be None
    
    if self.head is None:
      return None
    
    old_head = self.head
    old_value = old_head.value
    
    self.head = old_head.next
    self.head.prev = None
    
    # This is the case when there is only one item in the list.
    # if new head is none, set tail to be none, assuming we deleted the last item in the list
    if self.head is None:  
      self.tail = None
    
    # Cleaning up
    del(old_head)
    
    return old_value

  def add_to_tail(self, value):  # O(1)
    
    # The insert_after() method takes care of creating a new node and setting up the prev and next
    
    if self.tail is None:  # list is empty
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
      return
    
    self.tail.insert_after(value) # insert after the current tail
    self.tail = self.tail.next  # change the tail to be the new node
    
  def remove_from_tail(self):  # O(1)
    
    if self.tail is None:
      return None
      
    old_tail = self.tail
    old_value = old_tail.value
    
    self.tail = old_tail.prev
    self.tail.next = None
    
    # This is the case when there is only one item in the list.
    # if new head is none, set tail to be none, assuming we deleted the last item in the list
    if self.tail is None:  
      self.head = None
    
    # Cleaning up
    del(old_tail)
    
    return old_value

  def move_to_front(self, node):  # O(1)
    
    # If there is only one item in the list
    if self.head is self.tail:
      return
    
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
      
    self.head.prev = node
    node.next = self.head
    node.prev = None
    self.head = node
    
  def move_to_end(self, node):  # O(1)
    
    # If there is only one item in the list
    if self.head is self.tail:
      return
    
    if node.prev is not None:
      node.prev.next = node.next
    if node.next is not None:
      node.next.prev = node.prev
      
    self.tail.next = node
    node.prev = self.tail # set the current tail to be the node's prev
    node.next = None
    self.tail = node

  def delete(self, node):  # O(1)
    node.delete()
    
  def get_max(self):  # O(n)
    
    current_max = None  # O(1)  
    current_node = self.head  # O(1)
    
    while current_node is not None:  # O(n)
      if current_max is None or current_node.value > current_max:  # O(1)
        current_max = current_node.value  # O(1)
        
      current_node = current_node.next  # O(1)
    
    return current_max  # O(1)


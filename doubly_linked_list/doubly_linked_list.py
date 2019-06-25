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


  #i think we might need these methods
  #get value of next node
  def get_value(self):
      return self.value

  def get_next(self):
      return self.next_node

    #set the next node allows you to get the next node
  def set_next(self, new_next_node):
        #set this node's next_node reference to the passed in node
      self.next_node = new_next_node

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

  #add_to_head replaces the head of the list with a new value that is passed in
  def add_to_head(self, value):
    #initialize a node with a value
    new_node = Node(value, None)

    #if the list is empty
    if not self.head:
      self.head = new_node
      self.tail = new_node

    #if the list has one item
    elif not self.head.get_next():
      new_node.set_next = self.head
      self.head = new_node

    #if the list has 2 or more items
    else:
      prev_head = self.head
      self.head = new_node
      self.head.set_next(prev_head)
    

  #remove_from_head removes the head node and returns the value stored in it
  def remove_from_head(self):
    #if the linked list is empty, return none
    #if linked list has one value this also will have the same return
    if not self.head:
      return None

    #if the linked list has more than 1 value
    else:
      value = self.head.get_value()
      self.head = self.head.get_next()
      return value

  #add_to_tail replaces the tail of the list with a new value that is passed in
  def add_to_tail(self, value):
    #initialize a node with a value
    new_node = Node(value, None)

    #check if no head
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    #if our list is not empty add new node to tail
    else:
      #set current tail's next reference to the new node that we passed in
      self.tail.set_next(new_node)
      #state the linked list's tail
      self.tail = new_node

  #remove_from_tail removes the tail node and returns the value stored in it
  def remove_from_tail(self):
    #if linked list is empty return none
    #also if there is only one value in the linked list
    if not self.tail:
      return None

    #if linked list has more than one element
    else:
      value = self.tail.get_value()
      self.tail = self.tail.get_next()
      return value

  #move_to_front takes a reference to a node in the list and 
  # moves it to the front of the list, shifting all other list nodes down
  def move_to_front(self, node):
    #if the node is already in the front
    if node is self.head:
      return None

    value = node.value

    #if the node is currently the tail
    elif node is self.tail:
      self.remove_from_tail()
      self.add_to_head(value)
    
    else:
      node.delete()
      self.add_to_head(value)


  #move_to_end takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up
  def move_to_end(self, node):
    #if the node is already at the end
    if node is self.tail:
      return None

    value = node.value

    #if the node is currently the head
    elif node is self.head:
      self.remove_from_head()
      self.add_to_tail(value)

    else:
      node.delete()
      self.add_to_tail(value)


  #delete takes a reference to a node in the list and removes it from the list. 
  # The deleted node's previous and next pointers should point to each afterwards
  def delete(self, node):
    #if the list is empty
    if not self.head and not self.tail:
      return None

    #if one element
    if self.head == self.tail:
      self.head = None
      self.tail = None


    

  #get_max returns the maximum value in the list.
  def get_max(self):
    #if the list is empty
    if not self.head:
      return None

    max_value = self.head.value
    current = self.head

    #if the list has one or more items
    while current:
      if current.value > max_value:
        max_value = current.value

      current = current.next
    return max_value

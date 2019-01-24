#ListNode class is already done,comments represent guidance on what is happening

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

#brought over methods from single linked list
  def get_value(self):
    return self.value

  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next= new_next
  

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.max = None

  def add_to_head(self, value):
  #create a new node instance 
    new_node = ListNode(value)

  #1st set next property of new node instance to head
  #2nd set head property of new node instance to the new node (new_node)
    new_node.next = self.head
    self.head = new_node

    if self.head is None:
       self.tail = new_node

  def remove_from_head(self):
    #set the node that will be removed, which is it's self
    remove_node = self
    
    if self.head == None:
      return self.head
    
    else:
      return_val = self.head.get_value()
      self.head = self.head.get_next()
    
      if self.head is None:
          self.tail = None

      return return_val

  def add_to_tail(self, value):
    #create new node, and set prev property to the tail
    new_node = ListNode(value)
    new_node.prev = self.tail

    #then set current tail next property to the new node
    self.tail.next = new_node

    # and if the head and the tail are none then set the head and tail to the new node
    if self.head is None and self.tail is None:
      self.tail = new_node
      self.head = new_node
      #if not, just set the tail to new node
    else:
      self.tail = new_node


  def remove_from_tail(self): 
    # set self tail to node for removal and set previous node to the previous node of the tail
    remove_node = self.tail 
    prev_node = self.tail.prev

    #then, set the next node of the previous node to none
    prev_node.next = None

    #finally, set current tail to the previous node and return value of removed node
    self.tail = prev_node

    return remove_node.value
    
  def move_to_front(self, node):
    # delete the node and add it to the head
    node.delete
    self.add_to_head(self,node.value)

  def move_to_end(self, node):
    
    if node.prev is not None:
      node.prev.next = node.next

    if node.next is not None:
      node.next.prev = node.prev

    self.tail.next = node

    node.prev = self.tail
    node.next = None

    self.tail = node
    

  def delete(self, node):
  # set the next node to the nodes next node and the previous node to the nodes previous node
    next_node = node.next 
    previous_node = node.prev
   
    # swap next and previous node
    previous_node.next = next_node
    next_node.prev = previous_node

  def get_max(self):
    #REMEMBER come back to modify for double link exercise 
    current_node = self.head
    max_value = 0
    if current_node != None:
      while current_node != None:
        temp_value = current_node.get_value()
        if temp_value > max_value  :
          max_value = temp_value
        else:
          current_node = current_node.get_next()
      return max_value

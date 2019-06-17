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

  def printList(self):
    curr_node = self.head
    list_str = ""
    while(curr_node != None):
      list_str += "[" +str(curr_node.prev) + "," + str(curr_node.value) + "," + str(curr_node.next) + "] "
      curr_node = curr_node.next
    print(list_str)

  def add_to_head(self, value):
    #replace existing head with a new head with a value of value
    if value != None:
      if self.length > 0:
        self.head.insert_before(value)
        self.head = self.head.prev
      else:
        self.head = ListNode(value)
        self.tail = self.head
      self.length+=1

  def remove_from_head(self):
    #remove head node and return value in it
    if self.head != None:
      value = self.head.value
      if self.length > 1:
        new_head = self.head.next
        self.head.delete()
        self.head = new_head
      else:
        self.head = None
        self.tail = None
      self.length-=1
      return value
    else:
      return None

  def add_to_tail(self, value):
    #if there is no head and "Add_to_tail" is called, does it get added to head instead?
    if value != None:
      if self.length > 0:
        self.tail.insert_after(value)
        self.tail = self.tail.next
      else:
        self.tail = ListNode(value)
        self.head = self.tail
      self.length+=1

  def remove_from_tail(self):
    #remove tail and return its value
    if self.tail != None:
      value = self.tail.value
      if self.length > 1:
        new_tail = self.tail.prev
        self.tail.delete()
        self.tail = new_tail
      else:
        self.head = None
        self.tail = None
      self.length-=1
      return value
    else:
      return None
    
  def move_to_front(self, node):
    #moves specified node to front (head)
   
    curr_prev = node.prev
    curr_next = node.next
    curr_prev_next = None
    curr_next_prev = None

    if curr_prev != None:
      if curr_next != None:
        curr_next.prev = curr_prev
        curr_prev.next = curr_next
      else:
        #this node was the tail and now curr_prev needs to become tail
        curr_prev.next = None
        self.tail = curr_prev
    #else: current node already was head
    
    prev_head = self.head
    self.head = node
    node.prev = None
    node.next = prev_head
    prev_head.prev = node

    # assumptions: b/c this is "moving a node", this node is already in the list.
    # therefore length is >= 1
    # could already be head or tail
    # edge test case: length = 2 (swapping head and tail)



  def move_to_end(self, node):
    #moves specified node to end (tail)
    
    curr_prev = node.prev
    curr_next = node.next
    curr_prev_next = None
    curr_next_prev = None

    if curr_next != None:
      if curr_prev != None:
        curr_next.prev = curr_prev
        curr_prev.next = curr_next
      else:
        #this node was the head and now curr_next needs to become head
        curr_next.prev = None
        self.head = curr_next
    #else: current node already was tail
    
    prev_tail = self.tail
    self.tail = node
    node.prev = prev_tail
    node.next = None
    prev_tail.next = node

    # assumptions: b/c this is "moving a node", this node is already in the list.
    # therefore length is >= 1
    # could already be head or tail
    # edge test case: length = 2 (swapping head and tail)

  def delete(self, node):
    if node!=None:
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        #is head?
        if node.prev == None:
          self.head = node.next
        #is tail?
        elif node.next == None:
          self.tail = node.prev
      node.delete()
      self.length-=1
    
  def get_max(self):
    if self.length == 0:
      return None
    else:
      curr_node = self.head
      max = self.head.value
      while(curr_node != None):
        if curr_node.value > max:
          max = curr_node.value
        curr_node = curr_node.next
      return max
'''
#personal tests
node = ListNode(1)
dll = DoublyLinkedList(node)
dll.printList()
dll.add_to_tail(30)
dll.printList()
'''




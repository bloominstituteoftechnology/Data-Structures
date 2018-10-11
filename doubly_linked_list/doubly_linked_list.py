class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    node=ListNode(value) #creating a node for the passed value

    if self.value==None and self.prev==None: #checking for empty list 
      self.value=node
    elif self.next==None: #checking if current node is the tail or last node
      node.prev=self.value
      self.next=node
    else:                  #checking if the node lies between 2 other nodes
      node.next=self.next
      self.next=node
      node.prev=self.value

  def insert_before(self, value):
    node=ListNode(value)
    if self.value==None and self.prev==None:  #checking for empty list 
      self.prev=node
    elif self.next==None: #checking if current node is the tail or last node
      node.prev=self.prev
      node.next=self.value
      self.prev=node
    else:                 #checking if the node lies between 2 other nodes
      node.prev=self.prev
      node.next=self.value
      self.prev=node

  def delete(self):
    if self.value==None and self.prev==None:  #checking for empty list 
      self.value=None
    elif self.next==None:  #checking if current node is the tail or last node
      self.prev.next=None
      self.value=None
    elif self.prev==None:#checking if the node to be deleted is head
      self.val=None
      self.next=None  
    else:                   #checking if the node lies between 2 other nodes
      self.next.prev=self.prev
      self.prev.next=self.next
      self.value=None

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)

  def remove_from_head(self):
    self.head.delete()

  def add_to_tail(self, value):
    self.tail.insert_after(value)

  def remove_from_tail(self):
    self.tail.delete()

  def move_to_front(self, node):
    

  def move_to_end(self, node):
    pass

  def delete(self, node):
    

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    # set the new node as a new ListNode
    new_node = ListNode(value)

    # set the current node to this node
    current_node = self 

    # set the previous_node to the current nodes prev
    prev_node = current_node.prev 
    # set the other node to the current node next
    next_node = current_node.next

    # set the previous of the new node to the current node
    new_node.prev = current_node

    # set the prev of the new node to the next node
    new_node.next = next_node

    # set the next node of the current node to the new node
    current_node.next = new_node

  def insert_before(self, value):
    # set the new node as a new ListNode
    new_node = ListNode(value)

    # set the new nodes prev to the nodes prev
    new_node.prev = self.prev

    # set new nodes next to this node
    new_node.next = self

    # set this prev to the new node
    self.prev = new_node

  def delete(self):
    # if the prev is not none set the self prev next to next
    if self.prev is not None:
      self.prev.next = self.next
    # if the next is not none set the next.prev to the prev
    if self.next is not None:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    # if there is no head then set head and tail to new listnodes with value
    if self.head is None:
      self.head = ListNode(value)
      self.tail = ListNode(value)
    else:
      # otherwise create a new node with value
      new_node = ListNode(value)

      # set the next node to current head
      new_node.next = self.head
      
      # set the heads previous head to the new node
      self.head.prev  = new_node
      
      # set the current head to the new_node
      self.head = new_node

  def remove_from_head(self):
    # set self to removal node
    removal_node = self
    
    # if the head is none the return the head
    if self.head == None:
      return self.head
    
    # otherwise set a ret_val to the current heads value and set the head to the next node
    else:
      ret_val = self.head.value
      self.head = self.head.next
      
      # if the head is none then set the tail to none and return the ret_val to the caller
      if self.head is None:
        self.tail = None

      return ret_val

  def add_to_tail(self, value):
    # set new node as a new list node with value
    new_node = ListNode(value)

    # set the prev of the new node to the current tail
    new_node.prev = self.tail

    # set the current tail to the next node with a value of the new node
    self.tail.next = new_node

    # if the head and the tail are none then set the head and tail to the new node
    if self.head is None and self.tail is None:
      self.tail = new_node
      self.head = new_node

    # otherwise just set the tail to the new node
    else:
      self.tail = new_node

  def remove_from_tail(self):
    # set self tail to removal node
    node_to_remove = self.tail 
    
    # set the previous node to the previous node of the tail
    previous_node = self.tail.prev
    
    # set the next node of the previous node to none
    previous_node.next = None
    
    # set the current tail to the previous node and return the removal nodes value to the caller
    self.tail = previous_node
    return node_to_remove.value

  def move_to_front(self, node):
    # delete the node and add the nodes value to the head
    node.delete
    self.add_to_head(node.value)

  def move_to_end(self, node):
    # delete the node and add the nodes value to the tail
    node.delete()
    self.add_to_tail(node.value)

  def delete(self, node):
    # set the next node to the nodes next node and the previous node to the nodes previous node
    next_node = node.next 
    previous_node = node.prev
    # swap the 2 nodes (next node) and (previous node)
    previous_node.next = next_node
    next_node.prev = previous_node

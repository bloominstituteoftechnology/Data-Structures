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
    new_node.set_prev(current_node)

    # set the prev of the new node to the next node
    new_node.set_next(next_node)

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
    # otherwise create a new node with value
    # set the next node to current head
    # set the heads previous head to the new node
    # set the current head to the new_node
    pass

  def remove_from_head(self):
    # set self to removal node
    # if the head is none the return the head
    # otherwise set a ret_val to the current heads value and set the head to the next node
    # if the head is none then set the tail to none and return the ret_val to the caller
    pass

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def __str__(self):
    return f'Node Value: {self.value}'

  def insert_after(self, value):
    # if next is none, set next to value and prev to self
    # else, set the value of next to current node's next
    # and prev to current node and set the next node's prev
    # to value and current node's next to value
    if isinstance(value, ListNode) is False:
      value = ListNode(value)

    if self.next is None:
      self.next = value
      value.prev = self
    else:
      value.next = self.next
      value.prev = self
      self.next.prev = value
      self.next = value

  def insert_before(self, value):
    # if prev is none, set prev to value and next to self
    # else, set the value of prev to current node's prev
    # and next to current node and set the prev node's next
    # to value and current node's prev to value
    if isinstance(value, ListNode) is False:
      value = ListNode(value)

    if self.prev is None:
      self.prev = value
      value.next = self
    else:
      value.prev = self.prev
      value.next = self
      self.prev.next = value
      self.prev = value

  def delete(self):
    # if next is not none, set next's prev to current nodes
    # prev
    if self.next is not None:
      self.next.prev = self.prev
    
    # if prev is not none, set prev's nodes next to current
    # nodes next
    if self.prev is not None:
      self.prev.next = self.next

    # set current next and prev nodes to none and return
    # current node's value
    self.next = None
    self.prev = None
    return self.value

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    # insert the node before head
    self.head.insert_before(value)

    # if the head doens't contain a node after it,
    # set the tail to the head
    if self.head.next == None:
      self.tail = self.head

    # set head to the prev node on head
    self.head = self.head.prev

  def remove_from_head(self):
    # if head is not none and the next node is not none,
    # set head equal to the next node and return
    # the prev node deleted, else if next node is none, 
    # set value to the head's value
    # and set head and tail to none and return the value, 
    # else, if head does not exist, return none
    if self.head is not None:
      if self.head.next is not None:
        self.head = self.head.next
        return self.head.prev.delete()
      else:
        value = self.head.value
        self.head = None
        self.tail = None
        return value
    return None

  def add_to_tail(self, value):
    # insert the new node after the tail
    self.tail.insert_after(value)

    # if node before tail is none, set head equal to tail
    if self.tail.prev is None:
      self.head = self.tail
    
    # set tail equal to the next node after tail
    self.tail = self.tail.next

  def remove_from_tail(self):
    # if tail is not none, set the tail to the prev node
    # and delete the next node after the tail
    if self.tail is not None:
      self.tail = self.tail.prev
      return self.tail.next.delete()

  def move_to_front(self, node):
    node.delete()
    self.add_to_head(node)

  def move_to_end(self, node):
    node.delete()
    self.add_to_tail(node)

  def delete(self, node):
    node.delete()

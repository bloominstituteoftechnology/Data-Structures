"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    # wrap in Node instance
    new_node = Node(value, None)
    # check if there is no head
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      # set the current tail 's next reference to the new node
      self.tail.set_next(new_node)
      # update the List's tail reference
      self.tail = new_node
    print('added', self.tail.get_value())


  def remove_head(self):
    # check to see if there is a head
    if not self.head:
      return None
    #check if the head node has a next node
    if not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    else:
      value = self.head.get_value()
      self.head = self.head.get_next()
      return value

    # prev = None
    # head = self.head
    # curr = self.value
    # while head:
    #     if head.getData() == value:
    #         if prev:
    #             prev.setNextNode(curr.getNextNode())
    #         else:
    #             self.head = head.getNextNode()
    #         return True
                
    #     prev = head
    #     curr = head.getNextNode()

            
    #     return curr


  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the current node
    current = self.head
    #walk along the list so that as current is a Node
    while current:
      #return True if the current value we're looking at matches our target
      if current.get_value() == value:
        return True
      # update our current refence
      current = current.get_next()
    return False





  #   prev = None
  #   head = self.head
  #   curr = self.value
  #   while head:
  #       if head.getData() == value:
  #           if prev:
  #               prev.setNextNode(curr.getNextNode())
  #           else:
  #               self.head = head.getNextNode()
  #           return True
                
  #       prev = head
  #       curr = head.getNextNode()
            
  #       return curr

  
  
  
  def get_max(self):
    if not self.head
      return None
    max_value = self.head.get_value()
    current = self.head.get_next()
    while current:
      if current.get_value() > max_value()

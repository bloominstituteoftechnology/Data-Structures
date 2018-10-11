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
    new_node = Node(value)

    if self.head == None:
      self.head = new_node 
    else:
      self.tail.set_next(new_node)
    
    self.tail = new_node


  def remove_head(self):
    first_node = self.head

    if first_node == None: 
      return None
    else:
      self.head = first_node.get_next()
      if not self.head:
        self.tail = None
        
    return first_node.get_value()
    

  def contains(self, value, node="start"):
    # L = LinkedList
    node = self.head if node == "start" else node

    if node != None:
      node_value = node.get_value()
      if node_value == value:
        return True
      else:
        next_node = node.get_next()

        return self.contains(value, next_node)
      # if get_naxt 
    else:
      return False

  def get_max(self, node="start", maxNode=None):
    # need reference point 
    if node == None:
      return maxNode

    node = self.head if node == "start" else node
    if node != None: 
      node_value = node.get_value()
      if maxNode == None or node_value > maxNode:
        maxNode = node_value
      #   return self.get_max(node, maxNode)
      # else:
      next_node = node.get_next()
      return self.get_max(next_node, maxNode)
    else:
      return maxNode
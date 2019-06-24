class Node:
  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_node):
    self.next_node = new_node

  def set_value(self, value):
    self.value =  value

class Linked_List: 
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail  = new_node 


  def remove_head(self):
    if self.head = None:
      return None
    elif self.head == self.tail:
      del_value = self.head.get_value()
      self.head = None
      self.tail = None
      return del_value
    else:
      del_value = self.head.get_value()  
      self.head = self.head.get_next()
      return del_value



class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = Linked_List()

  def enqueue(self, item):
    # pass
  
  def dequeue(self):
    # pass
    

  def len(self):
    # pass
